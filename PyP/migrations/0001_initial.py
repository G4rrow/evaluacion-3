# Generated by Django 4.0.5 on 2022-06-29 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Productoa')),
                ('nombreProducto', models.CharField(max_length=50, verbose_name='Nombre del Producto')),
                ('imgProducto', models.ImageField(default='/default/default-prod.png', upload_to='Productos')),
                ('Precio', models.IntegerField(verbose_name='Precio del producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PyP.categoria')),
            ],
        ),
    ]
