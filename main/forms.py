from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user_profile', 'profile']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'password1')

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        exclude = ['post_rated', 'score']
