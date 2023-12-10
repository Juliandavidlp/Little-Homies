#Acá defino las rutas que van a permitir mi aplicación.


from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('mascotas/', views.index,name='inicio_app'),
    path('getmascotas/', views.get_mascotas,name='getmascotas_app'),

]