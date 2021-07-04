from django.urls import path

from Textile_Market.textile_app.views import home_page, about_us, offers, sign

urlpatterns = [
    path('', home_page, name='home'),
    path('about', about_us, name='about us'),
    path('offers', offers, name='offers'),
    path('sign', sign, name='sign'),
]