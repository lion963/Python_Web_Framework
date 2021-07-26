from django.urls import path

from Textile_Market.textile_auth.views import logout_view, SignInView, RegisterView

urlpatterns = [
    # path('login', login_view, name='login'),
    path('login', SignInView.as_view(), name='login'),
    # path('register', register, name='register'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', logout_view, name='logout'),
]