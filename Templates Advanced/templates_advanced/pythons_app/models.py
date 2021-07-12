from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Python(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    image = CloudinaryField('image')
    # image = models.ImageField(upload_to='images')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    image = CloudinaryField('image')