from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    likes = models.IntegerField()
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    comments = models.TextField(null = True)
    user = models.ForeignKey(User)


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    user_bio = models.TextField()
    user = models.ForeignKey(User)
    last_update = models.DateTimeField(auto_now_add=True, null=True)
    images_uploaded = models.ForeignKey(Image)
