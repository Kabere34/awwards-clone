from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from .models import *
from . forms import *

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def login(request) :
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
          email = form.cleaned_data['email']
          password = form.cleaned_data['password1']
          user = authenticate(email=email, password1=password)
          return redirect('index')
    else:
      form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def index(request):
   posts = Post.objects.all()
   profile = Profile.objects.all()
   current_user = request.user
   context ={
   "posts":posts ,
   "profile":profile
   }
   return render(request, 'main/index.html', context)

def new_post(request):
   current_user=request.user
   if request.method == 'POST':
      form=UploadForm(request.POST, request.FILES)
      if form.is_valid():
         post=form.save(commit=False)
         post.user_profile=current_user
         post.save()
      return redirect('index')
   else:
      form=UploadForm()
   return render(request, 'main/new_post.html', {"form": form})


# def profile(request):
#   '''
# 	Method that fetches a users profile page
# 	'''
#   current_user =request.user
#   user=User.objects.all()
#   profile_image=Profile.objects.filter(user=request.user.pk)
#   print('hello')
#   return render(request,"main/profile.html" ,{"profile":profile, "current_user":current_user})


# def profile(request):
#    profile=User.Objects.get(username=username)
#    try:
#       profile_info=Profile.get_profile(profile.id)
#    except:
#         profile_info = Profile.filter_by_id(profile.id)
#    posts = Post.get_profile_image(profile.id)
#    title = f'@{profile.username}'
#    context={'title':title, 'profile':profile, 'profile_info':profile_info, 'posts':posts}
#    return render(request, 'main/profile.html',context )

# @login_required(login_url='login')
# def profile(request, username):
#     return render(request, 'profile.html')


