from django.shortcuts import render

# Create your views here.
def lista_productos(request):
    productos = [
        {
            'id': 1,
            'nombre': 'Kit de Frenos (Pastillas)',
            'precio': 35000,
            'descripcion': 'Pastillas de cerámica de alto rendimiento para frenado silencioso.',
            'imagen': 'img/pastillas_freno.jpg',
            'stock': 12,
            'oferta': False
        },
        {
            'id': 2,
            'nombre': 'Aceite Sintético 5W-30',
            'precio': 42000,
            'descripcion': 'Protección avanzada para el motor en condiciones extremas (4 Litros).',
            'imagen': 'img/aceite_motor.jpg',
            'stock': 25,
            'oferta': True
        },
        {
            'id': 3,
            'nombre': 'Batería 12V 75Ah',
            'precio': 115000,
            'descripcion': 'Batería de libre mantenimiento con alta capacidad de arranque en frío.',
            'imagen': 'img/bateria.jpg',
            'stock': 8,
            'oferta': False
        },
        {
            'id': 4,
            'nombre': 'Filtro de Aire',
            'precio': 12500,
            'descripcion': 'Filtro de alta eficiencia para optimizar el consumo de combustible.',
            'imagen': 'img/filtro_aire.jpg',
            'stock': 40,
            'oferta': False
        },
        {
            'id': 5,
            'nombre': 'Amortiguadores Delanteros',
            'precio': 85000,
            'descripcion': 'Par de amortiguadores reforzados para mayor estabilidad y confort.',
            'imagen': 'img/amortiguadores.jpg',
            'stock': 4,
            'oferta': True
        },
        {
            'id': 6,
            'nombre': 'Bujías de Iridium',
            'precio': 28000,
            'descripcion': 'Set de 4 bujías de larga duración para una mejor combustión.',
            'imagen': 'img/bujias.jpg',
            'stock': 15,
            'oferta': False
        },
        {
            'id': 7,
            'nombre': 'Correa de Distribución',
            'precio': 55000,
            'descripcion': 'Correa dentada de alta resistencia, compatible con motores 1.6 y 2.0.',
            'imagen': 'img/correa_distribucion.jpg',
            'stock': 0,
            'oferta': False
        },
        {
            'id': 8,
            'nombre': 'Kit de Embrague (Clutch)',
            'precio': 195000,
            'descripcion': 'Kit completo: Prensa, disco y rodamiento de empuje.',
            'imagen': 'img/embrague.jpg',
            'stock': 3,
            'oferta': True
        },
        {
            'id': 9,
            'nombre': 'Radiador de Aluminio',
            'precio': 130000,
            'descripcion': 'Radiador de alta disipación térmica para evitar sobrecalentamientos.',
            'imagen': 'img/radiador.jpg',
            'stock': 2,
            'oferta': False
        },
        {
            'id': 10,
            'nombre': 'Luces LED H7',
            'precio': 18000,
            'descripcion': 'Bombillos de luz blanca ultra brillante para mayor visibilidad nocturna.',
            'imagen': 'img/luces_led.jpg',
            'stock': 20,
            'oferta': True
        },
    ]
    
    context_catalogo = {'productos': productos}
    return render(request, 'catalogo/lista_productos.html', context_catalogo)
        


