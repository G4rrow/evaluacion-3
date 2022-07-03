from django.shortcuts import render
from .models import (
    Categoria,
    Producto
)
# Create your views here.
def home(request):

    Categorias=Categoria.objects.all()
    data = {}
    data["categorias"]=Categorias
    return render(request, 'home.html', data)

def index(request):
    data = {}
    productoF = []
    producto_fav = Producto.objects.filter(favorito = True)
    productos = Producto.objects.all()
    cont = 1
    list_temp = []
    for pf in producto_fav:
        if cont <= 3:
            list_temp.append(pf)
            cont += 1
        elif cont == 4:
            cont = 1
            productoF.append(list_temp)
            list_temp = [pf]
    else:
        if len(list_temp) > 0:
            productoF.append(list_temp)

    data['productos'] = productos
    data["productoF"] = productoF

    return render(request, 'index.html', data)

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')    