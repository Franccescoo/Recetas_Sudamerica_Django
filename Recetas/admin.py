from django.contrib import admin
from .models import Usuario, Nacionalidad, Receta
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Nacionalidad)
admin.site.register(Receta)