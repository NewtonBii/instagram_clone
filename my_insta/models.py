from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User)


class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    likes = models.IntegerField()
    date_create = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comments)
    user = models.ForeignKey(User)


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    user_bio = models.TextField()
    user = models.ForeignKey(User)
