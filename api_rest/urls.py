from django.urls import path
from api_rest.views import listado_usuarios, addUsuario, modEliminarUsuario
from api_rest.viewsLogin import ini_user
urlpatterns = [
    path('listado_usuarios/',listado_usuarios,name="listado_usuarios"),
    path('addUsuario/',addUsuario,name="addUsuario"),
    path('modEliminarUsuario/<id>',modEliminarUsuario,name="modEliminarUsuario"),
    path('ini_user/',ini_user,name="ini_user"),
    
]