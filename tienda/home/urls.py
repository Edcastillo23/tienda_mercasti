from django.urls import path
from . import views

urlpatterns = [
    #en las comillas pondremos la direccion web
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    
    ]