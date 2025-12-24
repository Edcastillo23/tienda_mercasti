from django.db import models

# Create your models here.
class Producto(models.Model):
    # 'id' se crea automáticamente por Django como un AutoField (Clave Primaria)
    
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()  
    descripcion = models.TextField()
    
    # En base de datos se guarda la ruta como texto
    imagen = models.CharField(max_length=200, default='imagengenerica.jpg')
    
    stock = models.IntegerField(default=0)
    oferta = models.BooleanField(default=False)
    
    # Recomendación extra: añade la categoría para poder filtrar
    #categoria = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre
