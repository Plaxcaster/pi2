# arquivo experiencein/experiencein/urls.py
from django.contrib import admin
from django.urls import path
from perfis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
]