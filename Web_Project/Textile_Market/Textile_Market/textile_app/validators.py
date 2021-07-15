from django.core.exceptions import ValidationError


def validate_quantity(value):
    if value<=0:
        raise ValidationError('Quantity must be bigger than "0"')