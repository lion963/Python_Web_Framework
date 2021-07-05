from django.urls import path

from Textile_Market.textile_app.views import home_page, about_us, offers, sign, create_offer, offer_details

urlpatterns = [
    path('', home_page, name='home'),
    path('about', about_us, name='about us'),
    path('offers', offers, name='offers'),
    path('sign', sign, name='sign'),
    path('create', create_offer, name='create offer'),
    path('offer_details', offer_details, name='details offer')
]