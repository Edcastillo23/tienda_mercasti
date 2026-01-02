import random
import string
import unicodedata
from django.db import models

# Función auxiliar para normalizar texto (quitar tildes)
def eliminar_tildes(cadena):
    if not cadena:
        return ""
    # Normaliza y filtra caracteres que no sean acentos
    return ''.join((c for c in unicodedata.normalize('NFD', cadena) if unicodedata.category(c) != 'Mn'))

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()  
    descripcion = models.TextField()
    marca = models.CharField(max_length=50, null=True, blank=True)
    sku = models.CharField(max_length=20, unique=True, null=True, blank=True)
    imagen = models.CharField(max_length=200, default='imagengenerica.jpg')
    stock = models.IntegerField(default=0)
    oferta = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    # NUEVO: Campo para búsqueda optimizada sin tildes
    busqueda_index = models.TextField(editable=False, blank=True)

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        # 1. LÓGICA DEL SKU: Generar si no existe
        if not self.sku:
            while True:
                nuevo_sku = "REP-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                if not Producto.objects.filter(sku=nuevo_sku).exists():
                    self.sku = nuevo_sku
                    break
        
        # 2. LÓGICA DEL BUSCADOR: Limpiar tildes y guardar en minúsculas
        # Combinamos nombre, descripción y marca para que el buscador sea potente
        texto_para_indexar = f"{self.nombre} {self.descripcion} {self.marca if self.marca else ''}"
        self.busqueda_index = eliminar_tildes(texto_para_indexar).lower()

        super().save(*args, **kwargs)