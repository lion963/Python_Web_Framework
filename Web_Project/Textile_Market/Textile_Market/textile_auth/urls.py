from django.urls import path

from Textile_Market.textile_auth.views import login_view, register, logout_view

urlpatterns = [
    path('login', login_view, name='login'),
    path('register', register, name='register'),
    path('logout', logout_view, name='logout'),
]