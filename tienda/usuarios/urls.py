from django.urls import path
from . import views

urlpatterns = [
    #en las comillas pondremos la direccion web
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('', views.home_view, name='home'),
    ]