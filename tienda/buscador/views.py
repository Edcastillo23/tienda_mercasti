from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from catalogo.models import Producto
from django.db.models import Q


# Create your views here.
import unicodedata
from django.db.models import Q

def buscar_productos(request):
    query_original = request.GET.get('q', '').strip()
    
    # Función local para limpiar la búsqueda del usuario
    query_limpia = ''.join((c for c in unicodedata.normalize('NFD', query_original) 
                        if unicodedata.category(c) != 'Mn')).lower()

    if query_limpia:
        # Buscamos en el campo especial que ya está limpio en la DB
        productos = Producto.objects.filter(
            busqueda_index__icontains=query_limpia
        ).order_by('id')
    else:
        productos = Producto.objects.all().order_by('id')

    # Paginación (puedes dejar la que ya tenías)
    paginator = Paginator(productos, 2)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'buscador/resultados_busqueda.html', {
        'productos': page_obj,
        'query': query_original # Devolvemos la original para que el usuario la vea bien
    })
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    context_detalle = {'producto': producto}

    return render(request, 'catalogo/detalle_producto.html', context_detalle)


