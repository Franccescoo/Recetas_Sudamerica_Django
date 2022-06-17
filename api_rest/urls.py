from django.urls import path
from api_rest.views import listado_usuarios, addUsuario, modEliminarUsuario, listado_recetas, addReceta,modEliminarReceta
from api_rest.viewsLogin import ini_user
urlpatterns = [
    path('ini_user/',ini_user,name="ini_user"),

    path('listado_usuarios/',listado_usuarios,name="listado_usuarios"),
    path('addUsuario/',addUsuario,name="addUsuario"),
    path('modEliminarUsuario/<id>',modEliminarUsuario,name="modEliminarUsuario"),

    path('listado_recetas/',listado_recetas,name="listado_recetas"),
    path('addReceta/',addReceta,name="addReceta"),
    path('modEliminarReceta/<id>',modEliminarReceta,name="modEliminarReceta"),
    
]