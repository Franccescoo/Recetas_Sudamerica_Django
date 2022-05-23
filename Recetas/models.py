from django.db import models

# Create your models here.

class TIPO_USUARIO(models.Model):
    idTipoUsuario = models.AutoField(primary_key=True, verbose_name="ID autoincrementable de tipo de usuario")
    nomTipoUsuario = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nomTipoUsuario

class USUARIO(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nomUsuario = models.CharField(max_length=30, blank=False, null=False)
    apellidoCompleto = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=30, null=False)
    foto = models.ImageField(upload_to="foto_perfil")
    TIPO_USUARIO = models.ForeignKey(TIPO_USUARIO, on_delete= models.CASCADE)

    def __str__(self) :
            return self.nomUsuario

class NACIONALIDAD(models.Model):
    idNacionalidad = models.AutoField(primary_key=True)
    nomNacionalidad = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) :
            return self.nomNacionalidad

class RECETA(models.Model):
    idReceta = models.AutoField(primary_key=True)
    nomReceta = models.CharField(max_length=30, blank=False, null=False)
    ingrediente = models.CharField(max_length=100, null=False, blank=False)
    preparacion = models.CharField(max_length=250, null=False, blank=False)
    fotoReceta = models.ImageField(upload_to="foto_receta")
    USUARIO = models.ForeignKey(USUARIO, on_delete= models.CASCADE)
    NACIONALIDAD = models.ForeignKey(NACIONALIDAD, on_delete= models.CASCADE)

    def __str__(self) :
            return self.nomReceta








