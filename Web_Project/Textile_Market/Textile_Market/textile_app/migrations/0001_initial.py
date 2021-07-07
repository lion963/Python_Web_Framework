# Generated by Django 3.2.4 on 2021-07-05 18:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('garment_type', models.TextField(max_length=30)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('description', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]