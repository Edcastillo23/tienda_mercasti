from django.shortcuts import render
from catalogo.models import Producto

# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all()
    
    context_catalogo = {'productos': productos}
    return render(request, 'catalogo/lista_productos.html', context_catalogo)
        


