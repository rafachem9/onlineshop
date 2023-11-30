import os
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from gestionPedidos.forms import FormularioContacto


# Create your views here.
def home(request):
    return render(request, 'index.html')


def busqueda_productos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    if request.GET['producto']:

        # mensaje = "Árticulo buscado: %r" %request.GET['producto']
        product = request.GET['producto']

        if len(product) > 20:

            mensaje = 'Texto de búsqueda demasiado largo'
        else:

            # incontrains funciona a un like de sql
            articulos = Articulos.objects.filter(nombre__contains=product)
            return render(request, "resultados_busqueda.html", {"articulos": articulos, "query": product})

    else:

        mensaje = 'No has introducido nada'

    return HttpResponse(mensaje)


def contacto(request):
    if request.method == 'POST':

        mi_formulario = FormularioContacto(request.POST)

        if mi_formulario.is_valid():
            infform = mi_formulario.cleaned_data

            send_mail(infform['asunto'], infform['mensaje'],
                      infform.get('email', ''), [os.getenv('EMAIL_CONTACT')
                                                 ], )

            return render(request, 'gracias.html')

    else:

        mi_formulario = FormularioContacto()

    return render(request, 'formulario_contacto.html', {'form': mi_formulario})
