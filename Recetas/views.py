from django.shortcuts import render, redirect
from .models import USUARIO
# Create your views here.

def index(request):
    return render(request,'Recetas/index.html')

def Login(request):
    return render(request,'Recetas/Login.html')

def registrarse(request):
    return render(request,'Recetas/registrarse.html')

def contact(request):
    return render(request,'Recetas/contact.html')

def Vista_de_Admin(request):
    return render(request,'Recetas/Vista_de_Admin.html')

def Ver_Receta_Admin(request):
    return render(request,'Recetas/Ver_Receta_Admin.html')

def Ver_Usuario_Admin(request):
    return render(request,'Recetas/Ver_Usuario_Admin.html')

def Editar_Recetas_Admin(request):
    return render(request,'Recetas/Editar_Recetas_Admin.html')

def menu(request):
    return render(request,'Recetas/menu.html')
    
def aatest(request):
    return render(request,'Recetas/aatest.html')

def aatest(request):
    return render(request,'Recetas/aatest.html')

def contact(request):
    return render(request,'Recetas/contact.html')

def Creacion_Recetas(request):
    return render(request,'Recetas/Creacion_Recetas.html')

def Editar_Recetas_Admin(request):
    return render(request,'Recetas/Editar_Recetas_Admin.html')

def Editar_Recetas(request):
    return render(request,'Recetas/Editar_Recetas.html')

def index(request):
    return render(request,'Recetas/index.html')

def Login(request):
    return render(request,'Recetas/Login.html')

def menu(request):
    return render(request,'Recetas/menu.html')

def modificar_usuario_admin(request):
    return render(request,'Recetas/modificar_usuario_admin.html')

def modificar_vista_usuario(request):
    return render(request,'Recetas/modificar_vista_usuario.html')

def RecetaArgentina(request):
    return render(request,'Recetas/RecetaArgentina.html')

def RecetaChile(request):
    return render(request,'Recetas/RecetaChile.html')

def RecetaEcuador(request):
    return render(request,'Recetas/RecetaEcuador.html')

def RecetaPeru(request):
    return render(request,'Recetas/RecetaPeru.html')

def RecetasBrasil(request):
    return render(request,'Recetas/RecetasBrasil.html')

def RecetasColombia(request):
    return render(request,'Recetas/RecetasColombia.html')

def RecetasVenezuela(request):
    return render(request,'Recetas/RecetasVenezuela.html')

def RecetaUruguay(request):
    return render(request,'Recetas/RecetaUruguay.html')

def registrarse(request):
    return render(request,'Recetas/registrarse.html')

def Ver_Receta_Admin(request):
    return render(request,'Recetas/Ver_Receta_Admin.html')

def Ver_Receta_Usuario(request):
    return render(request,'Recetas/Ver_Receta_Usuario.html')

def Ver_Usuario_Admin(request):
    return render(request,'Recetas/Ver_Usuario_Admin.html')

def Vista_de_Admin(request):
    return render(request,'Recetas/Vista_de_Admin.html')

def Vista_de_Usuario(request):
    return render(request,'Recetas/Vista_de_Usuario.html')

