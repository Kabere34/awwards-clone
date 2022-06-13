from csv import field_size_limit
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import status
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
      model=Post
      fields=('id','name', 'image', 'description', 'live_link')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
      model=Post
      fields=('avatar','bio','contact')
