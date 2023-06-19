# Importar librerias necesarias
from django.urls import path

# Importar la vista de la aplicación principal
from . import views

urlpatterns = [
    # Ruta de la página principal
    path('', views.home, name='home'),
]