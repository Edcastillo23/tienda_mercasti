from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from catalogo.models import Producto

# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all().order_by('id')

    paginator = Paginator(productos, 4)  # Mostrar 4 productos por página
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context_catalogo = {'productos': page_obj}
    return render(request, 'catalogo/lista_productos.html', context_catalogo)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    relacionados = Producto.objects.exclude(id=producto.id)[:4]

    context_detalle = {'producto': producto, 
                    'relacionados': relacionados}

    return render(request, 'catalogo/detalle_producto.html', context_detalle)
        

