from django.db import models

# Create your models here.


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoria")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Id de Productoa")
    nombreProducto = models.CharField(max_length=50, verbose_name="Nombre del Producto")
    imgProducto = models.ImageField(upload_to="Productos/", blank=False, null=False, default='/default/default-prod.jpg')
    precio = models.IntegerField(verbose_name="Precio del producto")
    favorito = models.BooleanField(verbose_name="Favoritio", default=False, blank=False, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField(verbose_name="descripcion", default="")

    def __str__(self):
        return self.nombreProducto




