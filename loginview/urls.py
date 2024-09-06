
from os import name
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls , name='adminu'),
    path('',include('auth_user.urls')),
]
