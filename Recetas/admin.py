from django.contrib import admin
from .models import Usuario, Nacionalidad, Alimento, Dieta, Receta, RolUsuario, Comentario, Valoracion
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Nacionalidad)
admin.site.register(Receta)
admin.site.register(RolUsuario)
admin.site.register(Comentario)
admin.site.register(Valoracion)
admin.site.register(Dieta)
admin.site.register(Alimento)