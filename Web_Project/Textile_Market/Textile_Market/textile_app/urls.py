from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Textile_Market.textile_app.views import home_page, about_us, offers, sign, create_offer

urlpatterns = [
    path('', home_page, name='home'),
    path('about', about_us, name='about us'),
    path('offers', offers, name='offers'),
    path('sign', sign, name='sign'),
    path('create', create_offer, name='create offer')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)