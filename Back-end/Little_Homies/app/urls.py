#Acá defino las rutas que van a permitir mi aplicación.

from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('', views.index,name='inicio_app'),
    path('mascotas/', views.get_mascotas,name='getmascotas_app'),
    path('mascotas/<int:id>/', views.detail_mascota),   
]


