# Generated by Django 4.2.7 on 2023-12-10 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='banner',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='Listado de mascotas'),
        ),
    ]
