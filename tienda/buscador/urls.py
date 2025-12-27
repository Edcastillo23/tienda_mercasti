from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscar_productos, name='buscar_productos'),
    
]