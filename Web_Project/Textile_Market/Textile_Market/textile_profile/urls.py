from django.urls import path

from Textile_Market.textile_profile.views import ProfileView, UpdateProfileView, DeleteProfileView

urlpatterns = [
    # path('profile', profile, name='profile'),
    path('profile', ProfileView.as_view(), name='profile'),
    # path('update/<int:pk>', update_profile, name='update'),
    path('update/<int:pk>', UpdateProfileView.as_view(), name='update'),
    # path('delete/<int:pk>', delete_profile, name='delete'),
    path('delete/<int:pk>', DeleteProfileView.as_view(), name='delete'),
]