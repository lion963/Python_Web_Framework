from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from Textile_Market.textile_app.models import AddOffer
from Textile_Market.textile_profile.models import Profile


class AddOfferTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Test', password='1234')
        self.profile = Profile.objects.create(user=self.user, first_name='sdafsad', last_name='asdfasdf', type='company', telephone='085236',image='')

    def test_correct_model(self):
        offer = AddOffer(profile=self.profile, garment_type='pants', quantity=200, description='some',
                         image='')
        offer.full_clean()
        offer.save()
        self.assertIsNotNone(offer)

    def test_incorrect_quantity(self):
        offer = AddOffer(profile=self.profile, garment_type='pants', quantity=0, description='some',
                         image='')

        with self.assertRaises(ValidationError) as context:
            offer.full_clean()
            offer.save()
        self.assertIsNotNone(context.exception)

class ProfileTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Test', password='1234')

    def test_when_correct_data(self):
        profile = Profile(user=self.user,
                          first_name='Pesho',
                          last_name='Peshov',
                          type='company',
                          telephone='0885236125',
                          image='')
        profile.full_clean()
        profile.save()
        self.assertIsNotNone(profile)

    def test_when_telephone_is_incorrect(self):
        profile = Profile(user=self.user,
                         first_name='Pesho',
                         last_name='Peshov',
                         type='company',
                         telephone='08852asdf125',
                         image='')
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)