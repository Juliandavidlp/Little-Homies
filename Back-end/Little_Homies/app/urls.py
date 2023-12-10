#Acá defino las rutas que van a permitir mi aplicación.


from django.urls import path, re_path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('mascotas/', views.index,name='inicio_app'),
    path('getmascotas/', views.get_mascotas,name='getmascotas_app'),   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #Habilita la posibilidad de acceder a los archivos de la carpeta media
    # en producción o desarrollo.


