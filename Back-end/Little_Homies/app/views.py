from django.shortcuts import render
from django.http import HttpResponse

#Importo el modelo de mascota.
from app.models import mascota

#Importo el serializador que había creado...
from app import serializers

#Importo clases y funciones de la librería rest_framework
from rest_framework import status
from rest_framework.decorators import api_view, api_view
from rest_framework.response import Response

def index(request):
    return HttpResponse('<h1>Hola mundo con Django.</h1>')
  
@api_view(['GET']) #Por el decorador solo puedo acceder si la petición es GET.
def get_mascotas(request):
    """
    ----La lista de las mascotas----
    """
    #Con lo siguiente se buscan los registros guardados en la base del modelo Mascota.
    mascotas=mascota.objects.all()
    #Tengo que serializar las múltiples instancias del modelo...
    serializer=serializers.MascotaSerializer(mascotas,many=True)
    #Y hecho eso, devuelvo un Response, que es una clase que me permite devolver 
    #una respuesta que cumpla los estándares de API-REST.
    return Response(serializer.data)


api_view(['GET'])
def detail_mascota(request,id):
    """
    Para mostrar una mascota en adopción.
    """
    #Comprobamos si el registro existe.
    if not mascota.objects.exists(pk=id):
        return Response(status=status.HTTP_404_NOT_FOUND, data='El recurso no ha sido encontrado.')
    
    #Busco una mascota a partir del id.
    mascota=mascota.objects.get(pk=id)
    
    #Repito el paso de la lista...
    serializer=serializers.MascotaSerializer(mascota) 
    return Response(serializer.data)
    #Y por último, devuelvo el objeto en formato API REST.