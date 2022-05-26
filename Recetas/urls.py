from django.urls import URLPattern, path
from .views import index, aatest, contact, Creacion_Recetas, Editar_Recetas_Admin, Editar_Recetas, Login, menu, modificar_usuario_admin, modificar_vista_usuario, RecetaArgentina, RecetaChile, RecetaEcuador, RecetaPeru, RecetasBrasil, RecetasColombia, RecetasVenezuela, RecetaUruguay, registrarse, Ver_Receta_Admin, Ver_Receta_Usuario, Ver_Usuario_Admin, Vista_de_Admin, Vista_de_Usuario, registrarUsuario


urlpatterns = [
    path('',index,name="index"),
    path('aatest/',aatest,name="aatest"),
    path('contact/',contact,name="contact"),
    path('Creacion_Recetas/',Creacion_Recetas,name="Creacion_Recetas"),
    path('Editar_Recetas_Admin/',Editar_Recetas_Admin,name="Editar_Recetas_Admin"),
    path('Editar_Recetas/',Editar_Recetas,name="Editar_Recetas"),
    path('Login/',Login,name="Login"),
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
    path('registrarUsuario', registrarUsuario, name="registrarUsuario"),
    path('Ver_Receta_Admin/',Ver_Receta_Admin,name="Ver_Receta_Admin"),
    path('Ver_Receta_Usuario/',Ver_Receta_Usuario,name="Ver_Receta_Usuario"),
    path('Ver_Usuario_Admin/',Ver_Usuario_Admin,name="Ver_Usuario_Admin"),
    path('Vista_de_Admin/',Vista_de_Admin,name="Vista_de_Admin"),
    path('Vista_de_Usuario/',Vista_de_Usuario,name="Vista_de_Usuario"),
]
