from django.conf.urls import url
from django.contrib.auth.models import User
from django.test import TestCase

from Textile_Market.textile_app.models import Profile, AddOffer


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