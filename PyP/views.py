from urllib import request
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import (
    Categoria,
    Producto
)
from .forms import (
    ProductoForm,
    EliminarProductoForm,
    EditarProductoForm
)
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):

    Productos=Producto.objects.all()
    data = {}
    data["productos"]=Productos
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

    data['productos'] = productos[:8]
    data["productoF"] = productoF
    
    return render(request, 'index.html', data)

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')    

def descripcion(request):
    return render(request, 'descripcion.html')        

@login_required(login_url = 'auth:login')
def listarProductosAdmin(request):
    data = {}
    productos = Producto.objects.all()

    page = request.GET.get('page')
    paginator = Paginator(productos, 5)
    try:
        pag = paginator.page(page)
    except PageNotAnInteger:
        pag = paginator.page(1)
    except EmptyPage:
       pag = paginator.page(paginator.num_pages)
    
    data["pag"] = pag

    return render(request,'CRUD/listarProductos.html',data)

@login_required(login_url = 'auth:login')
def agregarProducto(request):
    data = {}
    if request.method == 'POST':
        data['form'] = ProductoForm(request.POST,request.FILES or None)
        if data['form'].is_valid():
            data['form'].save()
            return redirect('pyp:listaProductosAdmin')
    else:
        data['form'] = ProductoForm()

    return render(request,'CRUD/agregarProducto.html',data)

@login_required(login_url = 'auth:login')
def eliminarProducto(request,pk):
    data = {}
    producto = Producto.objects.get(idProducto = pk)
    data["img"] = producto.imgProducto

    if request.method == 'POST':

        data['form'] = EliminarProductoForm(request.POST,request.FILES or None, instance = producto, pk=pk)
        if data['form'].is_valid():
            producto.delete()
            return redirect('pyp:listaProductosAdmin')
    else:
        data['form'] = EliminarProductoForm(instance = producto, pk=pk)

    return render(request,'CRUD/eliminarProducto.html',data)

@login_required(login_url = 'auth:login')
def editarProducto(request,pk):
    data = {}
    producto = Producto.objects.get(idProducto = pk)
    data["img"] = producto.imgProducto

    if request.method == 'POST':

        data['form'] = EditarProductoForm(request.POST,request.FILES or None, instance = producto, pk=pk)
        if data['form'].is_valid():
            data['form'].save()
            return redirect('pyp:listaProductosAdmin')
    else:
        data['form'] = EditarProductoForm(instance = producto, pk=pk)

    return render(request,'CRUD/editarProducto.html',data)

def listarProductos(request):
    data = {}
    productos = Producto.objects.all()

    page = request.GET.get('page')
    paginator = Paginator(productos, 8)
    try:
        pag = paginator.page(page)
    except PageNotAnInteger:
        pag = paginator.page(1)
    except EmptyPage:
       pag = paginator.page(paginator.num_pages)
    
    data["pag"] = pag

    return render(request,'listaProductos.html',data)