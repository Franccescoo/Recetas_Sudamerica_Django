from django.contrib import admin
from .models import Dificultad, Usuario, TipoUsuario, Nacionalidad, Receta
# Register your models here.
admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(Nacionalidad)
admin.site.register(Receta)
admin.site.register(Dificultad)