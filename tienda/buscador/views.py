from django.shortcuts import render
from django.core.paginator import Paginator
from catalogo.models import Producto
from django.db.models import Q


# Create your views here.
def buscar_productos(request):
    query = request.GET.get('q', '')

    productos = Producto.objects.filter(
        Q(nombre__icontains=query) | Q(descripcion__icontains=query)
    ).order_by('id')

    paginator = Paginator(productos, 1)  # Mostrar 2 productos por página
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context_buscador = {
        'productos': page_obj,
        'query': query
    }
    return render(request, 'buscador/resultados_busqueda.html', context_buscador)