from django.urls import path
from .views import *

app_name = "pyp"
urlpatterns = [
    
    path('servicios/',servicios, name='servicios'),
    path('home/',home, name='home'),
    path('',index, name='index'),
    path('contacto/',contacto, name='contacto'),
    path('nosotros/',nosotros, name='nosotros'),
    path('descripcion/<pk>',descripcion, name='descripcion'),

    path('listar-productos/',listarProductos, name='listaProductos'),

    path('listar-productos-admin/',listarProductosAdmin, name='listaProductosAdmin'),
    path('agregar-producto/',agregarProducto, name='agregarProducto'),
    path('eliminar-producto/<pk>/',eliminarProducto, name='eliminarProducto'),
    path('editar-producto/<pk>/',editarProducto, name='editarProducto'),
]