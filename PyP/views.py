from django.shortcuts import render
from .models import Categoria
# Create your views here.
def home(request):

    Categorias=Categoria.objects.all()
    data = {}
    data["categorias"]=Categorias
    return render(request, 'home.html', data)

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def index(request):
    return render(request, 'index.html')    