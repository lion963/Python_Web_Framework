from django.urls import path

from Textile_Market.textile_auth.views import SignInView, RegisterView, LogoutView

urlpatterns = [
    # path('login', login_view, name='login'),
    path('login', SignInView.as_view(), name='login'),
    # path('register', register, name='register'),
    path('register', RegisterView.as_view(), name='register'),
    # path('logout', logout_view, name='logout'),
    path('logout', LogoutView.as_view(), name='logout'),
]