from dataclasses import field
from pyexpat import model
from django import forms
from  .models import Producto

class ProductoForm(forms.ModelForm):  
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto','precio','imgProducto','favorito','descripcion','categoria']
        labels={
            'idProducto':'Codigo del Producto',
            'nombreProducto':'Nombre del Producto',
            'precio':'Precio del Producto',
            'imgProducto':'Imagen del Producto',
            'favorito':'¿Es Favorito?',
            'descripcion':'Descripción Breve del Producto',
            'categoria':'Ingrese categoria',
        }


class EliminarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto','precio','favorito','descripcion']
        labels={
            'idProducto':'Codigo del Producto',
            'nombreProducto':'Nombre del Producto',
            'precio':'Precio del Producto',
            'descripcion':'Descripción Breve del Producto',
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
        self.fields['descripcion'].widget.attrs['readonly'] = True


class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto','precio','imgProducto','favorito','descripcion','categoria']
        labels={
            'idProducto':'Codigo del Producto',
            'nombreProducto':'Nombre del Producto',
            'precio':'Precio del Producto',
            'imgProducto':'Cambiar imagen del producto',
            'descripcion':'Descripción Breve del Producto',
            'favorito':'¿Es Favorito?',
            'categoria':'Ingrese categoria',
        }

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop('pk',None)
        produc = Producto.objects.get(idProducto=pk)
        super(EditarProductoForm, self).__init__(*args, **kwargs)
        
        self.fields['favorito'].widget.attrs['checked'] = produc.favorito


