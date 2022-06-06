from django.contrib import admin
from .models import Usuario, Nacionalidad, Receta, RolUsuario, Comentario
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Nacionalidad)
admin.site.register(Receta)
admin.site.register(RolUsuario)
admin.site.register(Comentario)
