import os
from os.path import join

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from Textile_Market.textile_app.forms import OfferForm
from Textile_Market.textile_auth.forms import LoginForm
from Textile_Market.textile_profile.forms import ProfileForm


class OfferFormTests(TestCase):

    def test_correct_data(self):
        data = {'garment_type': 'pants',
                'quantity': 200,
                'description': 'some descriptiom',
                'image': ''}
        form = OfferForm(data)
        self.assertTrue(form.is_valid())

    def test_quantity_less_than_1_data(self):
        data = {'garment_type': 'pants',
                'quantity': 0,
                'description': 'some descriptiom',
                'image': ''}
        form = OfferForm(data)
        self.assertFalse(form.is_valid())


class ProfileFormTest(TestCase):
    def test_correct_data(self):
        data = {'first_name': 'Pesho',
                'last_name': 'Peshov',
                'type': 'company',
                'telephone':'545435435',
                'image':''}
        form = ProfileForm(data)
        self.assertTrue(form.is_valid())

    def test_telephone_is_not_numeric(self):
        data = {'first_name': 'Pesho',
                'last_name': 'Peshov',
                'type': 'company',
                'telephone': '5454dsfsdafs35435',
                'image': ''}
        form = ProfileForm(data)
        self.assertFalse(form.is_valid())

class LoginFormTests(TestCase):
    # def test_if_credentials_is_valid(self):
    #     user = User.objects.create(username='asen', password='20232521a')
    #     data = {
    #         'username': 'asen',
    #         'password': '20232521a'
    #     }
    #     form = LoginForm(data)
    #     self.assertTrue(form.is_valid())

    def test_if_credentials_is_not_valid(self):
        data = {
            'username': 'Test',
            'password': ''
        }
        form = ProfileForm(data)
        self.assertFalse(form.is_valid())