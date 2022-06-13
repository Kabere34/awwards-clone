from csv import field_size_limit
from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
      model=Post
      fields=('id','name', 'image', 'description', 'live_link')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
      model=Post
      fields=('avatar','bio','contact')
