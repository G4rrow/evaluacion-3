# Generated by Django 4.0.5 on 2022-07-04 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyP', '0002_rename_precio_producto_precio_producto_favorito_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(default=True, verbose_name='descripcion'),
        ),
    ]
