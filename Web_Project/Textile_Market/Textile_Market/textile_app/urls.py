from django.urls import path

from Textile_Market.textile_app.views import home_page, about_us, offers, login_view, create_offer, offer_details, \
    register, profile, logout_view, update_profile, my_offers, page_401

urlpatterns = [
    path('', home_page, name='home'),
    path('about', about_us, name='about us'),
    path('offers', offers, name='offers'),
    path('my_offers', my_offers, name='my offers'),
    path('login', login_view, name='login'),
    path('create', create_offer, name='create offer'),
    path('offer_details', offer_details, name='details offer'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('logout', logout_view, name='logout'),
    path('update', update_profile, name='update'),
    path('page_401', page_401, name='page 401'),
]