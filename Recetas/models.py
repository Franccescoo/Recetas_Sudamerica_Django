from django.db import models

# Create your models here.

class RolUsuario(models.Model):
    idRol = models.AutoField(primary_key=True)
    nomRol = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) :
            return self.nomRol


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nomUsuario = models.CharField(max_length=30, blank=False, null=False)
    apellidoCompleto = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=30, null=False)
    foto = models.ImageField(upload_to="foto_perfil", default="foto_perfil/foto_perfil_default.png", blank='')
    contrasena = models.CharField(max_length=20, null=False, blank=False)
    RolUsuario = models.ForeignKey(RolUsuario, on_delete= models.CASCADE, default=1)

    def __str__(self) :
            return self.nomUsuario

class Nacionalidad(models.Model):
    idNacionalidad = models.AutoField(primary_key=True)
    nomNacionalidad = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) :
            return self.nomNacionalidad
            

class Receta(models.Model):
    idReceta = models.AutoField(primary_key=True)
    nomReceta = models.CharField(max_length=30, blank=False, null=False)
    ingrediente = models.CharField(max_length=1000, null=False, blank=False)
    preparacion = models.CharField(max_length=2000, null=False, blank=False)
    tiempo = models.IntegerField(null=False, blank=False)
    fotoReceta = models.ImageField(upload_to='foto_receta',default="foto_receta/foto_default_receta.png", blank='')
    Usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    Nacionalidad = models.ForeignKey(Nacionalidad, on_delete= models.CASCADE)

    def __str__(self) :
            return self.nomReceta


class Comentario(models.Model):
    idComentario        = models.AutoField(primary_key=True)
    nomComentario       = models.CharField(max_length=30, blank=False, null=False)
    emailComentario     = models.CharField(max_length=30, null=False)
    Mensaje             = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self) :
            return self.nomComentario

class Valoracion(models.Model):
    idValoracion        = models.AutoField(primary_key=True)
    mensajeValoracion   = models.CharField(max_length=1000, null=False, blank=False)
    estrellaValoracion  = models.IntegerField(null=False, blank=False)
    Usuario             = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    Receta              = models.ForeignKey(Receta, on_delete= models.CASCADE)






