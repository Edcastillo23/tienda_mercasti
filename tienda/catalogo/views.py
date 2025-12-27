from django.shortcuts import render
from django.core.paginator import Paginator
from catalogo.models import Producto

# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all().order_by('id')

    paginator = Paginator(productos, 2)  # Mostrar 4 productos por página
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context_catalogo = {'productos': page_obj}
    return render(request, 'catalogo/lista_productos.html', context_catalogo)
        

