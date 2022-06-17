from rest_framework import serializers
from Recetas.models import Usuario, Receta, Comentario


class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idUsuario','nomUsuario','apellidoCompleto','username','email','contrasena','RolUsuario']
class RecetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = ['idReceta','nomReceta','ingrediente','preparacion','tiempo','Usuario','Nacionalidad']

class ComentarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['idComentario','nomComentario','emailComentario','Mensaje']

