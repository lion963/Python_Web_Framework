from django.urls import path

from Textile_Market.textile_auth.views import register, logout_view, SignInView

urlpatterns = [
    # path('login', login_view, name='login'),
    path('login', SignInView.as_view(), name='login'),
    path('register', register, name='register'),
    path('logout', logout_view, name='logout'),
]