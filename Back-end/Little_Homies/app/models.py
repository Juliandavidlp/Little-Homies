from django.db import models

# Create your models here.
#La clase mascota hereda métodos y atributos de la clase model

class mascota(models.Model):

    title=models.CharField(max_length=100,verbose_name="Título")
    raza=models.CharField(max_length=100,verbose_name="Raza")
    año_de_nacimiento=models.DateField(null=True, verbose_name="Fecha de nacimiento")

    def __str__(self):
        return self.title
    