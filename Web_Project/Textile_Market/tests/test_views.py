from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory

from Textile_Market.textile_app.models import AddOffer
from Textile_Market.textile_profile.models import Profile


class TextileMarketViewTest(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.user = User.objects.create(username='Test', password='1234')
        self.profile = Profile.objects.create(user=self.user, first_name='sdafsad', last_name='asdfasdf',
                                              type='company', telephone='085236', image='')
        self.offer = AddOffer.objects.create(profile=self.profile, garment_type='pants', quantity=200)

    def test_getHomePage_should_render_template(self):
        response = self.test_client.get('')
        self.assertTemplateUsed(response, 'home_page.html')

    def test_offersView_emplate(self):
        response = self.test_client.get('/offers')
        offers = response.context['offers']
        self.assertTemplateUsed(response, 'offers.html')
