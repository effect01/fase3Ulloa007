
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name: forms.CharField(max_length=65, required=True)
    last_name: forms.CharField(max_length=65, required=True)
    class Meta:
        model = User
        fields = ['username', 'email',  'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name: forms.CharField(max_length=65, required=True)
    last_name: forms.CharField(max_length=65, required=True)
    class Meta:
        model = User
        fields = ['username', 'email',  'last_name', 'first_name']

class ProfileUpdateForm(forms.ModelForm):
    dateBirth = forms.fields.DateField( input_formats=['%dd/%m', '%dd/%m'],  widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Profile
        fields = ['image','dateBirth', 'code_number','phone_number']


class ProfilePointForm(forms.ModelForm):
    dateBirth = forms.fields.DateField( input_formats=['%dd/%m', '%dd/%m'],  widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Profile
        fields = ['image','dateBirth', 'code_number','phone_number']