from django.core.exceptions import ValidationError


def validate_phone(value):
    if not value.isnumeric():
        raise ValidationError('Telephon number must be all numeric.')



