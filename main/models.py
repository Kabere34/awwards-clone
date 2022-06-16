from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    avatar = models.ImageField(upload_to='images/', blank=True)
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    contact = models.EmailField(max_length=100, blank=True)
    user = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE, blank=True)

    def save_profile(self):
        self.save()

    class Meta:
        ordering = ['user']


class Post(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(max_length=255)
    live_link=models.URLField(blank=True)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts',blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def search_by_name(cls,search_term):
        post = cls.objects.filter(name__icontains=search_term)
        return post

class Ratings(models.Model):
    INPUT = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design=models.IntegerField(choices=INPUT, default=0, blank=True)
    usability=models.IntegerField(choices=INPUT, blank=True)
    content=models.IntegerField(choices=INPUT, blank=True)
    score=models.IntegerField(default=0, blank=True)
    post_rated = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='ratings',null=True)

    def save_comment(self):
        self.save()

