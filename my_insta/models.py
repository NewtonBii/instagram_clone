from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    user_bio = models.TextField()
    user = models.ForeignKey(User)
    last_update = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering =['-last_update']

    def save_profile(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    image_name = models.CharField(max_length=30, null=True)
    image_caption = models.TextField(null =True)
    likes = models.IntegerField(null =True)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    comments = models.TextField(null=True)
    profile = models.ForeignKey(Profile, null=True)

    class Meta:
       ordering = ['-date_uploaded']

    def save_image(self):
        self.save()

    @classmethod
    def search_by_user(cls, search_term):
        images = cls.objects.filter(image_caption__icontains=search_term)
        return images

    @classmethod
    def get_image_by_id(cls, image_id):
        images = cls.objects.get(id=image_id)
        return images
