from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import UserProfile

class UserForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Your first name...'}))
    last_name = forms.CharField(max_length=30, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Your last name...'}))
    username = forms.EmailField(max_length=254, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Email...'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Password...','class':'password'})
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password...','class':'password'})
    )
    )
    
 
    