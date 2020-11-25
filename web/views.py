
from django.http.request import HttpHeaders
from django.shortcuts import render , get_object_or_404,redirect
from django.urls.base import reverse_lazy
from django.views.generic import ListView , FormView  
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , FormMixin , UpdateView, DeleteView
from users.models import Profile
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
from .form import CommentForm  , CreatePostForm
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.decorators import login_required
from .serialize import *



def index(request):
    return render(request, 'web/index.html')
    
def about(request):
    return render(request,'web/views/about.html')

def home(request):
    return render(request, 'web/views/home.html')

def contact(request): 
    return render(request,'web/views/contact.html')

def register(request):
    return render(request,'web/views/register.html')


def library(request):
    context = {
        'posts':Post.objects.all(),
    }
    return render(request, 'web/views/post.html', context)


class AuthorCreateView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    model =Author
    template_name = 'web/views/add_genero.html'
    fields = '__all__'
    success_message = "El Genero %(last_name)s se ah creado con exito"
    def form_valid(self, form):
        return super().form_valid(form)

class GeneroCreateView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    model =GenBook
    template_name = 'web/views/add_author.html'
    fields = '__all__'
    success_message = "El Author %(last_name)s se ah creado con exito"
    def form_valid(self, form):
        return super().form_valid(form)

class PostCreateView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    model =Post
    template_name = 'web/views/add_post.html'
    form_class =CreatePostForm
    success_message = "El post<libro> %(title)s se ah creado con exito"
    def form_valid(self, form):
        form.instance.postedBy = self.request.user
        return super().form_valid(form)

class PostUpdateView( SuccessMessageMixin , LoginRequiredMixin, UserPassesTestMixin, UpdateView ):
    model = Post
    form_class =CreatePostForm
    template_name = 'web/views/add_post.html'
    success_message = "El post<libro> %(title)s se ah actualizado"
    
    def form_valid(self, form):
        form.instance.postedBy = self.request.user
        return super().form_valid(form)
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class PostDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'web/views/delete_post.html'
    success_url = '/'
    success_message = "El post<libro> %(title)s se ah eliminado con exito"
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
        
class PostListView(ListView):
    model = Post
    template_name = 'web/views/postList.html'
    context_object_name = 'posts'
    ordering = ['-data_posted']
    paginate_by= 3
    def get_queryset(self):
        try:
            gen = self.request.GET.get('gen') 
        except:    
            gen = ''
        try:
            author = self.request.GET.get('author') 
        except:    
            author = ''
        if (gen != '' and gen != None) and (author != '' and author != None) :
            object_list = self.model.objects.filter(genre = gen , author = author)
            
        elif gen != '' and gen != None :
            object_list = self.model.objects.filter(genre = gen)
        elif author != '' and author != None :
            object_list = self.model.objects.filter(author = author)
        else:
            object_list = self.model.objects.all().order_by('-data_posted')
        return object_list
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['gen'] = GenBook.objects.all()
        context['author'] = Author.objects.all()
        return context

class PostDetailView(FormMixin,DetailView):
    model = Post
    template_name = 'web/views/post_detail.html'
    form_class = CommentForm
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk} )
    def post(self, request, *args, **kwargs):       
        try:
            if not request.user.is_authenticated:
                return HttpResponseForbidden()
            nombre = request.POST['comment']
            tuser = Profile.objects.filter(user_id = self.request.user.id)
            self.object = self.get_object()
            form = self.get_form()
            if nombre:
                if form.is_valid():
                    tuser.update(points= tuser.get().points + 10)
                    return self.form_valid(form)    
            else:
                return self.form_invalid(form)
        except Exception as e:
            try:
                post = Post.objects.filter(id = self.kwargs['pk'] ).first()
                post.userbook_set.create(user_id= self.request.user.id)
                post.save()
                messages.success(self.request, f'Un libro se agregado a tu biblioteca ! !')
            except Exception as e:
                messages.warning(self.request, f'error : probablemente ya tienes este libro 🤣')
            return redirect('Booklary-profile')
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

        
class PostAdminListView(ListView):
    LOGIN_REQUIRED = True
    model = Post
    template_name = 'web/views/admin_post_admin.html'
    context_object_name = 'posts'
    ordering = ['-data_posted']
    paginate_by= 5


class AuthorAdminListView(ListView):
    LOGIN_REQUIRED = True
    model = Author
    template_name = 'web/views/admin_author.html'
    context_object_name = 'posts'
    paginate_by= 5
class GeneroAdminListView(ListView):
    LOGIN_REQUIRED = True
    model = GenBook
    template_name = 'web/views/admin_genero.html'
    context_object_name = 'posts'
    paginate_by= 5
class AddCommentForm(CreateView):
    model = Comment
    form_class = CommentForm 
    template_name= 'web/views/add_comment.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)


class GenViewSet(viewsets.ModelViewSet):
    queryset = GenBook.objects.all()
    serializer_class = GenSerializer
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
