from unicodedata import name
from django.urls import URLPattern, path
from .views import inicioAdmin,modificar_receta, eliminar_comentario, registrarComentario, Ver_Comen_Admin, usuario,recetas,login_app,aamate,eliminar_receta, Menu_Recetas, index, aatest, contact, registrarRecetas, Creacion_Recetas, registrarRecetas, Editar_Recetas_Admin, Editar_Recetas, Login, listadoRecetas, menu, modificar_usuario_admin, modificar_vista_usuario, RecetaArgentina, RecetaChile, RecetaEcuador, RecetaPeru, RecetasBrasil, RecetasColombia, RecetasVenezuela, RecetaUruguay, registrarse, Ver_Receta_Admin, Ver_Receta_Usuario, Ver_Usuario_Admin, Vista_de_Admin, Vista_de_Usuario, registrarUsuario,listadoRecetas,eliminar_usuario,modificar_receta_admin,modificar
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('Creacion_Recetas/<int:id>',Creacion_Recetas,name="Creacion_Recetas"),
    path('Ver_Usuario_Admin/<int:id>',Ver_Usuario_Admin,name="Ver_Usuario_Admin"),
    path('Vista_de_Admin/<int:id>',Vista_de_Admin,name="Vista_de_Admin"),
    path('Ver_Receta_Admin/<int:id>',Ver_Receta_Admin,name="Ver_Receta_Admin"),
    path('inicioAdmin/',inicioAdmin,name="inicioAdmin"),
    path('login_app/',login_app,name="login_app"),
    path('Vista_de_Usuario/<int:id>',views.Vista_de_Usuario,name="Vista_de_Usuario"),
    path('Ver_Comen_Admin/<int:id>',Ver_Comen_Admin,name="Ver_Comen_Admin"),
    path('Ver_Receta_Usuario/<int:id>',Ver_Receta_Usuario,name="Ver_Receta_Usuario"),
        path('eliminar_receta/<int:id>/<int:sesi>',eliminar_receta, name="eliminar_receta"),




    
    path('modificar_receta/<int:id>/<int:sesi>',modificar_receta,name="modificar_receta"),
    path('Editar_Recetas_Admin/<int:id>',Editar_Recetas_Admin,name="Editar_Recetas_Admin"),
    path('usuario/<int:id>/<int:sesi>',usuario,name="usuario"),
    path('recetas/<int:id>',recetas,name="recetas"),
    path('Menu_Recetas/',Menu_Recetas,name="Menu_Recetas"),
    path('Login/',Login,name="Login"),
   
    path('aamate/',aamate,name="aamate"),
    path('',index,name="index"),
    path('aatest/',aatest,name="aatest"),
    path('contact/',contact,name="contact"),
    path('Editar_Recetas/',Editar_Recetas,name="Editar_Recetas"),
    
    path('menu/',menu,name="menu"),
    path('modificar_usuario_admin/',modificar_usuario_admin,name="modificar_usuario_admin"),
    path('modificar_vista_usuario/',modificar_vista_usuario,name="modificar_vista_usuario"),
    path('RecetaArgentina/',RecetaArgentina,name="RecetaArgentina"),
    path('RecetaChile/',RecetaChile,name="RecetaChile"),
    path('RecetaEcuador/',RecetaEcuador,name="RecetaEcuador"),
    path('RecetaPeru/',RecetaPeru,name="RecetaPeru"),
    path('RecetasBrasil/',RecetasBrasil,name="RecetasBrasil"),
    path('RecetasColombia/',RecetasColombia,name="RecetasColombia"),
    path('RecetasVenezuela/',RecetasVenezuela,name="RecetasVenezuela"),
    path('RecetaUruguay/',RecetaUruguay,name="RecetaUruguay"),
    path('registrarse/',registrarse,name="registrarse"),
    path('registrarUsuario', views.registrarUsuario, name="registrarUsuario"),
    path('registrarRecetas/<int:id>', views.registrarRecetas, name="registrarRecetas"),
    path('registrarComentario', views.registrarComentario, name="registrarComentario"),
    
  


    path('listadoRecetas/',listadoRecetas, name="listadoRecetas"),
    path('registrarRecetas',registrarRecetas,name="registrarRecetas"),
    path('eliminar_usuario/<int:id>',eliminar_usuario, name="eliminar_usuario"),
    path('eliminar_comentario/<int:id>',eliminar_comentario, name="eliminar_comentario"),
    path('modificar_receta_admin',modificar_receta_admin,name="modificar_receta_admin"),
    path('modificar',modificar,name="modificar"),
]
