from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUsuarioAdmin(UserAdmin):
    model = Usuario
    
    # Qué columnas mostrar en la lista de usuarios
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_active')
    
    # Filtros laterales para búsqueda rápida
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    
    # Campos por los que se puede buscar en la barra superior
    search_fields = ('username', 'email')
    
    # Ordenar por defecto
    ordering = ('email',)

    # Esto asegura que el formulario de creación en el admin maneje bien el hashing de contraseñas
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email',)}),
    )

admin.site.register(Usuario, CustomUsuarioAdmin)