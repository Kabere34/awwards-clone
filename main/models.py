from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500)
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.bio

class Project(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='pics/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project")
    link =  models.URLField(max_length=200)
    design = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)
    vote_submissions = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    posted_by=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    comment_image=models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    comment=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.posted_by
