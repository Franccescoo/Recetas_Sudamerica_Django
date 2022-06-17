from django.urls import path
from api_rest.views import listado_mascotas, addMascota, modEliminarMascota
from api_rest.viewsLogin import ini_user
urlpatterns = [
    path('listado_mascotas/',listado_mascotas,name="listado_mascotas"),
    path('addMascota/',addMascota,name="addMascota"),
    path('modEliminarMascota/<codigo>',modEliminarMascota,name="modEliminarMascota"),
    path('ini_user/',ini_user,name="ini_user"),
]