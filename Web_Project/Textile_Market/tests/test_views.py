from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory

from Textile_Market.textile_app.models import AddOffer
from Textile_Market.textile_app.views import OfferDetailView, MyOffersView, OffersView
from Textile_Market.textile_auth.views import SignInView, RegisterView
from Textile_Market.textile_profile.models import Profile
from Textile_Market.textile_profile.views import ProfileView


class TextileMarket_textile_app_ViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.test_client = Client()
        self.user = User.objects.create(username='Test', password='1234')
        self.profile = Profile.objects.create(user=self.user, first_name='sdafsad', last_name='asdfasdf',
                                              type='company', telephone='085236', image='')
        self.offer = AddOffer.objects.create(profile=self.profile, garment_type='pants', quantity=200)

    def test_Page401View(self):
        response = self.test_client.get('')
        self.assertTemplateUsed(response, 'common/home_page.html')

    def test_OffersView(self):
        request = self.factory.get('/offers')
        request.user = self.user
        response = OffersView()
        self.assertEqual(response.response_class.status_code, 200)

    def test_MyOffersView(self):
        request = self.factory.get(f'/my_offers/{self.profile.id}')
        request.user = self.user
        response = MyOffersView()
        self.assertEqual(response.response_class.status_code, 200)

    def test_OfferDetailView(self):
        request = self.factory.get(f'/offer_details/{self.offer.id}')
        request.user = self.user
        response = OfferDetailView()
        self.assertEqual(response.response_class.status_code, 200)

    def test_CreateOfferView(self):
        data = {
            'profile': self.profile,
            'garment_type': 'pants',
            'quantity': 200}
        request = self.factory.post(f'/create/{self.profile.id}', data)
        request.user = self.user
        response = OfferDetailView()
        self.assertEqual(response.response_class.status_code, 200)


class TextileMarket_textile_auth_SignInView_RegisterView_Tests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.test_client = Client()
        self.user = User.objects.create(username='Test', password='1234')
        self.profile = Profile.objects.create(user=self.user, first_name='sdafsad', last_name='asdfasdf',
                                              type='company', telephone='085236', image='')
        self.offer = AddOffer.objects.create(profile=self.profile, garment_type='pants', quantity=200)

    def test_SignInView(self):
        data = {
            'username': self.user.username,
            'password': self.user.password,
        }
        request = self.factory.post('/login', data)
        request.user = self.user
        response = SignInView()
        self.assertEqual(response.response_class.status_code, 200)

    def test_RegisterView(self):
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
        response = RegisterView()
        self.assertEqual(response.response_class.status_code, 200)


class TextileMarket_textile_profilr_ProfileViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.test_client = Client()
        self.user = User.objects.create(username='Test', password='1234')
        self.profile = Profile.objects.create(user=self.user, first_name='sdafsad', last_name='asdfasdf',
                                              type='company', telephone='085236', image='')
        self.offer = AddOffer.objects.create(profile=self.profile, garment_type='pants', quantity=200)

    def test_ProfileView(self):
        request = self.factory.get('/profile')
        request.user = self.user
        response = ProfileView()
        self.assertEqual(response.response_class.status_code, 200)
