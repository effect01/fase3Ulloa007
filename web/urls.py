
from django.urls import path, include
from . import views 
from .route import router
from django.contrib.auth.decorators import login_required
from .views import  AddCommentForm, GeneroAdminListView,GeneroCreateView,PostListView,AuthorCreateView, PostDeleteView,AuthorAdminListView ,PostUpdateView,PostAdminListView, PostDetailView,AddCommentForm  , PostCreateView
urlpatterns = [
    path('contact/', views.contact, name='Booklary-contact'),
    path('', views.home, name='Booklary-index'),
    path('', include(router.urls)),
    path( 'api-auth/', include('rest_framework.urls', namespace='rest_framework') ),
    path('home/', views.home, name='Booklary-home'),
    path('library/',login_required(  PostListView.as_view( ) ) , name='Booklary-library'),
    path('about/', views.about, name='Booklary-about'),
    path('library/<int:pk>/', PostDetailView.as_view( ) , name='post-detail'),
    path('library/<int:pk>/comment/', AddCommentForm.as_view( ), name='add-comment' ),
    path('admin_post/add/', PostCreateView.as_view() , name='post_add' ),
    path('admin_post/', login_required(PostAdminListView.as_view()) , name='admin_post' ),
    path('admin_author/', login_required(AuthorAdminListView.as_view()) , name='admin_author' ),
    
    path('admin_genero/', login_required(GeneroAdminListView.as_view()) , name='admin_genero' ),
    
    path('admin_genero/add/', login_required(GeneroCreateView.as_view()) , name='genero_add' ),
    path('admin_author/add/', login_required(AuthorCreateView.as_view()) , name='author_add' ),
    path('admin_post/update/<int:pk>/', PostUpdateView.as_view( ) , name='post-update'),
    path('admin_post/delete/<int:pk>/', PostDeleteView.as_view( ) , name='post-delete'),
 

]