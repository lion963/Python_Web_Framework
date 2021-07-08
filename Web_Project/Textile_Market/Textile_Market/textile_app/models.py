from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

class AddOffer(models.Model):
    garment_type = models.TextField(max_length=30)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField(max_length=200)
    image = CloudinaryField('image')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    image = CloudinaryField('image')