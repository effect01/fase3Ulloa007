from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm , UserUpdateForm
from django.contrib.auth import  authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request,user)
            username = form.cleaned_data.get('username')
            nuevo_profile = Profile(user=user,dateBirth= '1999-12-12' ) 
            nuevo_profile.save()
            messages.success(request, f'Tu cuenta a sido creada, {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()  
    return render(request = request, template_name= 'users/register.html', context={'form': form})


@login_required
def profile(request):
    return render(request,'users/profile_content.html')
@login_required
def profile_config(request):
    if request.method == 'POST':
        u_form =  UserUpdateForm(request.POST, instance=request.user)
        p_form =  ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Tu cuenta a sido actualizada!')
            return redirect('Booklary-profile')
    else:
        u_form =  UserUpdateForm(instance=request.user)
        p_form =  ProfileUpdateForm(instance=request.user.profile)

    context ={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile_config.html', context)