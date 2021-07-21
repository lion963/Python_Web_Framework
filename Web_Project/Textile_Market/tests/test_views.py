from unittest.mock import patch
from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory

from Textile_Market.textile_app.models import AddOffer
from Textile_Market.textile_app.views import offer_details
from Textile_Market.textile_auth.views import login_view, register
from Textile_Market.textile_profile.models import Profile
from Textile_Market.textile_profile.views import profile


class TextileMarket_textile_appViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.test_client = Client()
        self.user = User.objects.create(username='Test', password='1234')
        self.profile = Profile.objects.create(user=self.user, first_name='sdafsad', last_name='asdfasdf',
                                              type='company', telephone='085236', image='')
        self.offer = AddOffer.objects.create(profile=self.profile, garment_type='pants', quantity=200)

    def test_getHomePage_should_render_template(self):
        response = self.test_client.get('')
        self.assertTemplateUsed(response, 'common/home_page.html')

    def test_offersView_template(self):
        response = self.test_client.get('/offers')
        offers = response.context['offers']
        self.assertTemplateUsed(response, 'common/offers.html')

    def test_my_offersView_template(self):
        response = self.test_client.get(f'/my_offers/{self.profile.id}')
        offers = response.context['offers']
        self.assertTemplateUsed(response, 'app/my_offers.html')

    def test_offer_details_View_template(self):
        request = self.factory.get(f'/offer_details/{self.offer.id}')
        request.user = self.user
        response = offer_details(request, self.offer.id)
        self.assertEqual(response.status_code, 200)

    def test_create_offer(self):
        data = {
            'profile': self.profile,
            'garment_type': 'pants',
            'quantity': 200}
        request = self.factory.post(f'/create/{self.profile.id}', data)
        request.user = self.user
        response = offer_details(request, self.profile.id)
        self.assertEqual(response.status_code, 200)




class TextileMarket_textile_authViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.test_client = Client()
        self.user = User.objects.create(username='Test', password='1234')
        self.profile = Profile.objects.create(user=self.user, first_name='sdafsad', last_name='asdfasdf',
                                              type='company', telephone='085236', image='')
        self.offer = AddOffer.objects.create(profile=self.profile, garment_type='pants', quantity=200)

    def test_login(self):
        data = {
                'username': self.user.username,
                'password': self.user.password,
        }
        # self.test_client.login()
        request = self.factory.post('/login', data)
        request.user = self.user
        response = login_view(request)
        # response = self.test_client.post('/login', data)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        data = {
            'username': 'test123',
            'password': '20232521a',
            'first_name': 'sdafsad',
            'last_name': 'asdfasdf',
            'type': 'company',
            'telephone': '085236'
        }
        request = self.factory.post('/register', data)
        request.user = self.user
        response = register(request)
        self.assertEqual(response.status_code, 200)


class TextileMarket_textile_profileViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.test_client = Client()
        self.user = User.objects.create(username='Test', password='1234')
        self.profile = Profile.objects.create(user=self.user, first_name='sdafsad', last_name='asdfasdf',
                                              type='company', telephone='085236', image='')
        self.offer = AddOffer.objects.create(profile=self.profile, garment_type='pants', quantity=200)

    def test_profile_view(self):
        request = self.factory.get('/profile')
        request.user = self.user
        response = profile(request)
        self.assertEqual(response.status_code, 200)