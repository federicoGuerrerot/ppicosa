from django.shortcuts import render

# Create your views here.

def home(request):
    """ Vista para la página de inicio """

    # El renderizado de la página se hace en el archivo base.html
    # en este se encuentra la estructura de la página
    # y el codigo JS para el funcionamiento de la página

    return render(request, 'base.html')
