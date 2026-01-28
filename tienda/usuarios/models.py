#from email.headerregistry import Group 
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Usuario(AbstractUser):
    email = models.EmailField(unique=True)

    grupos = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='Grupos a los que pertenece este usuario.',
        verbose_name='grupos',        
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios_user_set',
        blank=True, 
        help_text='Permisos específicos para este usuario.',
        verbose_name='user permissions',
    )
    def __str__(self):
        return self.username
