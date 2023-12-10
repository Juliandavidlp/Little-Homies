from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hola mundo con Django.</h1>')

def get_mascotas(request):
    return HttpResponse('<h2>Listado de mascotas.</h2>')
  

