from django.contrib import admin
from .models import Categoria, Producto
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('idCategoria','nombreCategoria')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=('idProducto','nombreProducto','imgProduc','precio','favorito','categoria')

    def imgProduc(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.imgProducto.url,
            width=50,
            height=50,
            )
    )
