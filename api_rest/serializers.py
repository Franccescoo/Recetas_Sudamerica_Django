from rest_framework import serializers
from Recetas.models import Usuario


class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idUsuario','nomUsuario','apellidoCompleto','username','email','foto','contrasena','RolUsuario']