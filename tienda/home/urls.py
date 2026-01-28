from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    #en las comillas pondremos la direccion web
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),

    ]