from dataclasses import field
from pyexpat import model
from django import forms
from  .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto','precio','imgProducto','favorito','categoria']
        labels={
            'idProducto':'Codigo del Producto',
            'nombreProducto':'Nombre del Producto',
            'precio':'Precio del Producto',
            'imgProducto':'Imagen del Producto',
            'favorito':'¿Es Favorito?',
            'categoria':'Ingrese categoria',
        }

