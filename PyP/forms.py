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


class EliminarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto','precio','favorito']
        labels={
            'idProducto':'Codigo del Producto',
            'nombreProducto':'Nombre del Producto',
            'precio':'Precio del Producto',
            'favorito':'¿Es Favorito?',
        }

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop('pk',None)
        produc = Producto.objects.get(idProducto=pk)
        super(EliminarProductoForm, self).__init__(*args, **kwargs)
        
        self.fields['idProducto'].widget.attrs['readonly'] = True
        self.fields['nombreProducto'].widget.attrs['readonly'] = True
        self.fields['precio'].widget.attrs['readonly'] = True
        self.fields['favorito'].widget.attrs['checked'] = produc.favorito
        self.fields['favorito'].widget.attrs['disabled'] = True





