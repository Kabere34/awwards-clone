from django.shortcuts import render,redirect

from .models import *
from . forms import *

# Create your views here.
def index(request):
   posts = Post.objects.all()
   current_user = request.user
   context ={
   "posts":posts ,
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




