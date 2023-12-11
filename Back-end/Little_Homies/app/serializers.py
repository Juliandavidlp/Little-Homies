from rest_framework import serializers
from app.models import mascota


class MascotaSerializer (serializers.ModelSerializer):

    class Meta:
        model=mascota #El modelo con el que se va a corresponder el serializador...

        #Entonces defino los campos de la clase mascota que quiero serializar:
        fields=['id','title','descripción','año_de_nacimiento','banner']
