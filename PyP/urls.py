from django.urls import path
from .views import *

app_name = "pyp"
urlpatterns = [
    
    path('servicios/',servicios, name='servicios'),
    #path('home/',home, name='home'),
    path('',index, name='index'),
    path('contacto/',contacto, name='contacto'),
    path('nosotros/',nosotros, name='nosotros'),

    path('listar-productos',agregarProducto, name='listaProductos'),
]