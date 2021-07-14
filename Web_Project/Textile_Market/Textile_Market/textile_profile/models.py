from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

from Textile_Market.textile_profile.validators import validate_phone


class Profile(models.Model):
    TYPE_CHOICES = (
        ('company', 'company'),
        ('person', 'person')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    telephone = models.CharField(
        max_length=20,
        blank=False,
        validators=[validate_phone]
    )
    image = CloudinaryField('image')
