from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('page_401', views.page_401, name='page 401'),

]
