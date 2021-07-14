from django.urls import path

from Textile_Market.textile_profile.views import profile, update_profile, delete_profile

urlpatterns = [
    path('profile', profile, name='profile'),
    path('update/<int:pk>', update_profile, name='update'),
    path('delete/<int:pk>', delete_profile, name='delete'),
]