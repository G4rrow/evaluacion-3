from django.db import models

# Create your models here.


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoria")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre de la categoria")

    def str(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Id de Productoa")
    nombreProducto = models.CharField(max_length=50, verbose_name="Nombre del Producto")
    imgProducto = models.ImageField(upload_to="Productos", blank=False, null=False, default='/default/default-prod.png')
    Precio = models.IntegerField(verbose_name="Precio del producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def str(self):
        return self.nombreProducto




