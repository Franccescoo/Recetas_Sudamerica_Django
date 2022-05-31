from django.shortcuts import render, redirect
from .models import Usuario,Receta,Nacionalidad
# Create your views here.

def RecetaChile_copy(request):
    RecetasChile = Receta.objects.all()
    return render(request,'Recetas/RecetaChile_copy.html', {"RecetasChile": RecetasChile})

def aamate(request):
    return render(request,'Recetas/aamate.html')

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

def Editar_Recetas_Admin(request):
    return render(request,'Recetas/Editar_Recetas_Admin.html')

def Editar_Recetas(request):
    return render(request,'Recetas/Editar_Recetas.html')

def index(request):
    return render(request,'Recetas/index.html')

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
    

def Creacion_Recetas(request):
    Nacio = Nacionalidad.objects.all()
    contexto = {"lista_r":Nacio}
    return render(request,"Recetas/Creacion_Recetas.html",contexto)


def listadoRecetas(request):
    receta = Receta.objects.all()
    contexto = {"lista_m":receta}
    return render(request,"Recetas/Creacion_Recetas.html",contexto)


def registrarRecetas(request):
    imagen2 = request.FILES['imagen']
    nomreceta2 = request.POST['nomreceta']
    tiempo2 = request.POST['tiempo']
    idNacionalidad2 = request.POST['idNacio']
    ingredientes2 = request.POST['ingredientes']
    preparacion2 = request.POST['preparacion']

    Nacionalidad3 = Nacionalidad.objects.get(idNacionalidad = idNacionalidad2)

    Receta.objects.create(fotoReceta =imagen2, nomReceta =nomreceta2, ingrediente =ingredientes2, preparacion=preparacion2, tiempo=tiempo2, Nacionalidad=Nacionalidad3 )


def listadoUsuario(request):
    usuario = Usuario.objects.all()
    contexto = {"lista_u":usuario}
    return render(request,"Recetas/Ver_Usuario_Admin.html", contexto)


def registrarUsuario(request):
    nombre2 = request.POST['nomUser']
    apellido2 = request.POST['apeUser']
    nick = request.POST['nickUserName']
    foto2 = request.FILES['foto1']
    email2 = request.POST['email']
    contra2 = request.POST['password1']

    Usuario.objects.create(nomUsuario = nombre2, apellidoCompleto = apellido2, username = nick, email = email2, foto = foto2, contrasena = contra2)
    Nacio = Nacionalidad.objects.all()
    contexto = {"lista_r":Nacio}
    return render(request,"Recetas/Creacion_Recetas.html",contexto)
