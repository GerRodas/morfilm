# Generated by Django 4.0.6 on 2022-08-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morfi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargar_pelicula',
            name='imagen_comida',
            field=models.ImageField(blank=True, null=True, upload_to='image_foods'),
        ),
        migrations.AlterField(
            model_name='cargar_pelicula',
            name='imagen_film',
            field=models.ImageField(blank=True, null=True, upload_to='image_films'),
        ),
    ]
