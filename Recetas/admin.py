from django.contrib import admin
from .models import USUARIO, TIPO_USUARIO, NACIONALIDAD, RECETA
# Register your models here.
admin.site.register(USUARIO)
admin.site.register(TIPO_USUARIO)
admin.site.register(NACIONALIDAD)
admin.site.register(RECETA)