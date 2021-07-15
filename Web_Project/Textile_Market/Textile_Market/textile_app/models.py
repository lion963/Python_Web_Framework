from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator
from django.db import models

from Textile_Market.textile_app.validators import validate_quantity
from Textile_Market.textile_profile.models import Profile


class AddOffer(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    garment_type = models.TextField(max_length=30)
    quantity = models.IntegerField(validators=[validate_quantity])
    description = models.TextField(max_length=200)
    image = CloudinaryField('image', blank=True)