from django.db import models

# Create your models here.
#La clase mascota hereda métodos y atributos de la clase model

class mascota(models.Model):

    title=models.CharField(max_length=100,verbose_name="Nombre")
    descripción=models.CharField(max_length=500,verbose_name="Descripción")
    año_de_nacimiento=models.DateField(null=True, verbose_name="Fecha de nacimiento")
    banner=models.ImageField(upload_to='imagenes/',null=True, verbose_name='Listado de mascotas')

    def __str__(self):
        return self.title
    

