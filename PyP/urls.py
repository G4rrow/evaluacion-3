from django.urls import path
from .views import *

app_name = "pyp"
urlpatterns = [
    
    path('servicios/',servicios, name='servicios'),
    path('home/',home, name='home'),
    path('',index, name='index'),
    path('contacto/',contacto, name='contacto'),
    path('nosotros/',nosotros, name='nosotros'),
<<<<<<< HEAD
    path('descripcion/',descripcion, name='descripcion'),

=======
>>>>>>> 1f5627a4bac4a852fb67da9e4237d8be6afd3c7e
    path('listar-productos/',listarProductos, name='listaProductos'),

    path('listar-productos-admin/',listarProductosAdmin, name='listaProductosAdmin'),
    path('agregar-producto/',agregarProducto, name='agregarProducto'),
    path('eliminar-producto/<pk>/',eliminarProducto, name='eliminarProducto'),
    path('editar-producto/<pk>/',editarProducto, name='editarProducto'),
]