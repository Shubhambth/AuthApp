from os import name
from django.urls import path 

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='loginu'),
    path('register/', views.user_register, name='registeru'),
    path('logout/', views.user_logout,name='logoutu')
    
]