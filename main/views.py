from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *
from . forms import *
from django.db.models import Q
# from .permissions import IsAdminOrReadOnly

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
   ratings=Ratings.objects.all()
   current_user = request.user
   context ={
   "posts":posts ,
   "profile":profile,
   "ratings":ratings,
   }
   return render(request, 'main/index.html', context)

@login_required(login_url='login')
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

# @login_required(login_url='login')
# def profile(request):
#   '''
# 	Method that fetches a users profile page
# 	'''
#   current_user =request.user
#   user=User.objects.all()
#   profile_image=Profile.objects.filter(user=request.user.pk)
#   print('hello')
#   return render(request,"main/profile.html" ,{"profile":profile, "current_user":current_user})

def user_profile(request):
  user=request.user
  posts=Post.objects.filter(user_profile=user)


  return render(request,"main/profile.html" ,{ "current_user":user,"posts":posts})

@login_required(login_url='login')
def profile_edit(request,user_id):
   user= request.user
   form=NewProfileForm()
   if request.method == 'POST':
      form=NewProfileForm(request.POST,request.FILES)
      if form.is_valid():
         image=form.save(commit=False)
         image.user=user
         form.save()
         return redirect('profile')
      else:
         form=NewProfileForm()
   return render(request,'main/profile_edit.html',{"form":form})

@login_required(login_url='login')
def rate_post(request,pk):
   [design, usability, content]=[[0],[0],[0]]

   post=get_object_or_404(Post, pk=pk)
   current_user= request.user
   print(current_user,'heeeyyoo')
   print(current_user.id,'heeeyyoo2')
   if request.method == 'POST':
      form=RatingsForm(request.POST)
      [design, usability, content] = [[0], [0], [0]]
      if form.is_valid():
         form.save()
         rating=Ratings.objects.last()
         design=rating.design
         usability=rating.usability
         content=rating.content
         rating.post_rated=post
         rating.save()

         print (design, usability, content)
         post_ratings=Ratings.objects.filter(post_rated=post)
         post_design_ratings=[pr.design for pr in post_ratings]
         print(post_design_ratings)
         design_avg=0
         for value in post_design_ratings:
                design_avg += value
         print (design_avg/len(post_design_ratings))
         design_score= (design_avg/len(post_design_ratings))

         post_usability_ratings = [pr.usability for pr in post_ratings]
         print (post_usability_ratings)
         usability_avg=0
         for value in post_usability_ratings:
               usability_avg += value
         print (usability_avg/len(post_usability_ratings))
         usability_score= (usability_avg/len(post_usability_ratings))
         post_content_ratings = [pr.content for pr in post_ratings]
         print (post_content_ratings)
         content_avg = 0
         for value in post_content_ratings:
                content_avg += value
         print (content_avg / len(post_content_ratings))
         content_score = (content_avg / len(post_content_ratings))


         score =(design_score + usability_score + content_score)/3

         rating.score =score
         rating.save()

         score=rating.score
         print ("last score=" + str(score))

         return redirect('index')
   else:
      form = RatingsForm()
      return render(request,'main/single_post.html',{"user":current_user,"ratings_form":form})

def single_post(request, post_id):
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.all()
    ratings = Ratings.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = RatingsForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('index')

    else:
        form = RatingsForm
    context = {
        "profile": profile,
        "form": form,
        "post": post,
        "ratings": ratings,
        'post_id': post.id,
    }
    return render (request, 'main/single_post.html',context)



# def search_results(request):
#    post= Post.objects.all()
#    query=request.GET.get('query')
#    if query:
#       image=Post.objects.filter( Q(name__icontains=query))
#       # profile=Profile.objects.filter( Q(user__username__icontains=query) )
#       params = {
#           'image': image,

#           'post':post
#       }
#       return render(request, 'main/search.html', params)

def search_results(request):

    if "post" in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'main/search.html',{"message":message,"searched_posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'main/search.html',{"message":message})


class Postlist(APIView):
    def get(self, request, format=None):
        all_post = Post.objects.all()
        serializers = PostSerializer(all_post, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

   #  permission_classes = (IsAdminOrReadOnly,)


# class Profilelist(APIView):
#     def get(self, request, format=None):
#         all_profiles = Profile.objects.all()
#         serializers = PostSerializer(all_profiles, many=True)
#         return Response(serializers.data)

   #  def post(self, request, format=None):
   #      serializers = ProfileSerializer(data=request.data)
   #      if serializers.is_valid():
   #          serializers.save()
   #          return Response(serializers.data, status=status.HTTP_201_CREATED)
   #      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

   #  permission_classes = (IsAdminOrReadOnly,)
class Profilelist(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
