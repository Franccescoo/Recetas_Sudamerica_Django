from django.db import models

# Create your models here.

class TipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key=True, verbose_name="ID autoincrementable de tipo de usuario")
    nomTipoUsuario = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nomTipoUsuario

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nomUsuario = models.CharField(max_length=30, blank=False, null=False)
    apellidoCompleto = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=30, null=False)
    foto = models.ImageField(upload_to="foto_perfil", default="foto_perfil/foto_perfil_default", blank='')
    contrasena = models.CharField(max_length=20, null=False, blank=False)
    TipoUsuario = models.ForeignKey(TipoUsuario, on_delete= models.CASCADE)

    def __str__(self) :
            return self.nomUsuario

class Nacionalidad(models.Model):
    idNacionalidad = models.AutoField(primary_key=True)
    nomNacionalidad = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) :
            return self.nomNacionalidad

class Dificultad(models.Model):
    idDificultad = models.AutoField(primary_key=True)
    nomDificultad = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) :
            return self.nomDificultad
            

class Receta(models.Model):
    idReceta = models.AutoField(primary_key=True)
    nomReceta = models.CharField(max_length=30, blank=False, null=False)
    ingrediente = models.CharField(max_length=100, null=False, blank=False)
    preparacion = models.CharField(max_length=250, null=False, blank=False)
    tiempo = models.IntegerField(default=0 , null=False, blank=False)
    fotoReceta = models.ImageField(upload_to="foto_receta")
    Usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    Nacionalidad = models.ForeignKey(Nacionalidad, on_delete= models.CASCADE)

    def __str__(self) :
            return self.nomReceta








