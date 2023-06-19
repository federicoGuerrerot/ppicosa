from django.shortcuts import render

# Create your views here.

def home(request):
    """ Vista para la página de inicio """

    return render(request, 'base.html')
