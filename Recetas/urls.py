from django.urls import URLPattern, path
from .views import  index, Login, registrarse, contact, Vista_de_Admin, Ver_Receta_Admin, Ver_Usuario_Admin,Editar_Recetas_Admin, menu

urlpatterns = [
    path('',index,name="index"),
    path('Login/',Login,name="Login"),
    path('registrarse/',registrarse,name="registrarse"),
    path('contact/',contact,name="contact"),
    path('Vista_de_Admin/',Vista_de_Admin,name="Vista_de_Admin"),
    path('Ver_Receta_Admin/',Ver_Receta_Admin,name="Ver_Receta_Admin"),
    path('Ver_Usuario_Admin/',Ver_Usuario_Admin,name="Ver_Usuario_Admin"),
    path('Editar_Recetas_Admin/',Editar_Recetas_Admin,name="Editar_Recetas_Admin"),
    path('menu/',menu,name="menu"),
    
    
    

]