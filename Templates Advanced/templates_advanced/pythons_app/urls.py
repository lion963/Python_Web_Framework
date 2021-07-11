from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.IndexView.as_view(), name='index'),
    # path('create/', views.create, name="create"),
    path('create/', views.CreatePythonView.as_view(), name='create'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    # path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('page_401', views.page_401, name='page 401'),
    path('profile', views.profile_view, name='profile'),
    path('update', views.update_profile, name='update'),

]
