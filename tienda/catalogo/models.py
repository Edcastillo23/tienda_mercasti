import random
import string
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    # 'id' se crea automáticamente por Django como un AutoField (Clave Primaria)
    
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()  
    descripcion = models.TextField()
    marca = models.CharField(max_length=50, null=True, blank=True)
    sku = models.CharField(max_length=20, unique=True, null=True, blank=True)
    
    # En base de datos se guarda la ruta como texto
    imagen = models.CharField(max_length=200, default='imagengenerica.jpg')
    
    stock = models.IntegerField(default=0)
    oferta = models.BooleanField(default=False)
    
    # Relación con categoría
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        # Si el producto no tiene SKU, lo generamos
        if not self.sku:
            while True:
                nuevo_sku = "REP-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                # Nos aseguramos de que sea único en la base de datos
                if not Producto.objects.filter(sku=nuevo_sku).exists():
                    self.sku = nuevo_sku
                    break
        super().save(*args, **kwargs)
