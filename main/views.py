from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
   # posts = Post.all_posts()
   current_user = request.user

   # context ={

   # "posts":posts ,
   
   return render(request, 'index.html')

