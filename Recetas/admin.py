from django.contrib import admin
from .models import Usuario, TipoUsuario, Nacionalidad, Receta
# Register your models here.
admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(Nacionalidad)
admin.site.register(Receta)