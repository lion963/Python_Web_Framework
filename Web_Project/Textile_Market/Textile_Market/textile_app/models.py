from django.core.validators import MinValueValidator
from django.db import models

class AddOffer(models.Model):
    garment_type = models.TextField(max_length=30)
    quantity = models.ImageField(validators=[MinValueValidator(1)])
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images', null=True)