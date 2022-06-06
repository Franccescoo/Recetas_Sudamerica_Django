from email import message
from django.shortcuts import render, redirect
from .models import Usuario,Receta,Nacionalidad,RolUsuario,Comentario
from django.contrib import messages
# Create your views here.
def registrarRecetas(request,id):
    Usuario2         = request.POST['autor']
    imagen2          = request.FILES['imagen']
    nomreceta2       = request.POST['nomreceta']
    tiempo2          = request.POST['tiempo']
    idNacionalidad2  = request.POST['idNacio']
    ingredientes2    = request.POST['ingredientes']
    preparacion2     = request.POST['preparacion']

    Nacionalidad3    = Nacionalidad.objects.get(idNacionalidad = idNacionalidad2)
    Usuario3         = Usuario.objects.get(idUsuario = Usuario2)


    Receta.objects.create(Usuario=Usuario3,fotoReceta =imagen2, nomReceta =nomreceta2, ingrediente =ingredientes2, preparacion=preparacion2, tiempo=tiempo2, Nacionalidad=Nacionalidad3 )
    
    messages.success(request, 'Receta Registrada')

    sesion = Usuario.objects.get(idUsuario=id)
    contexto={
        "sesion":sesion
    }

    return redirect('index')

def Creacion_Recetas(request,id):
    sesion = Usuario.objects.get(idUsuario=id)
    Nacio = Nacionalidad.objects.all()
    contexto = {
        "sesion":sesion,
        "lista_r":Nacio}
    return render(request,"Recetas/Creacion_Recetas.html",contexto)

def Ver_Usuario_Admin(request,id):
    sesion = Usuario.objects.get(idUsuario = id)
    UserAdmin = Usuario.objects.all()
    contexto = {
        "usuario":UserAdmin,
        "sesion":sesion
        }
    return render(request,'Recetas/Ver_Usuario_Admin.html',contexto)

def login_app(request):
    us = request.POST['nomUser']
    cl = request.POST['pass']
    try:
        x = Usuario.objects.get(username = us, contrasena = cl)
        rol2 = RolUsuario.objects.get(nomRol = 'Administrador')

        if x.RolUsuario.nomRol == rol2.nomRol:
            contexto ={"sesion":x}
            return render(request, 'Recetas/inicioAdmin.html',contexto)
        else:
            contexto ={"sesion":x}
            return render(request, 'Recetas/inicioUser.html',contexto)

    except Usuario.DoesNotExist:
        # messages.error(request, 'Usuario y/o clave incorrecta')
        return redirect ('Login')


def inicioAdmin(request,sesion):

    contexto={
        "sesion":sesion
    }
    return render(request,'Recetas/inicioAdmin.html',contexto)



def Vista_de_Usuario(request,id):
    sesion = Usuario.objects.get(idUsuario=id)
    contexto={
        "sesion":sesion
    }
    return render(request,'Recetas/Vista_de_Usuario.html',contexto)

def Vista_de_Admin(request,id):
    sesion = Usuario.objects.get(idUsuario=id)
    contexto={
        "sesion":sesion
    }
    return render(request,'Recetas/Vista_de_Admin.html',contexto)


def usuario(request,id,sesi):
    sesion =Usuario.objects.get(idUsuario = sesi)
    usuario1 = Usuario.objects.get(idUsuario=id)
    receta1 = Receta.objects.all()
    RolUsuario1 = RolUsuario.objects.all()
    Recet = Receta.objects.all()
    
    contexto = {
        "sesion":sesion,
        "receta":receta1,
        "RolUsuario":RolUsuario1,
        "usuario":usuario1,
        "Recetas":Recet
    }
    
    return render(request,'Recetas/usuario.html',contexto)



def Login(request):
    return render(request,'Recetas/Login.html')



def registrarUsuario(request):
    nombre2     = request.POST['nomUser']
    apellido2   = request.POST['apeUser']
    nick        = request.POST['nickUserName']
    foto2       = request.FILES['foto1']
    email2      = request.POST['email']
    contra2     = request.POST['password1']

    try:
        x = Usuario.objects.get(username = nick)
        c = Usuario.objects.get(email = email2)
        messages.error(request, 'El nombre de usuario o correo ya estan ocupados')
        return redirect ('registrarse')

    except Usuario.DoesNotExist:
        messages.error(request, 'Cargando')
        Usuario.objects.create(nomUsuario = nombre2, apellidoCompleto = apellido2, username = nick, email = email2, foto = foto2, contrasena = contra2)
        sesion = Usuario.objects.get(username=nick)
        contexto ={
        "sesion":sesion
        }
        messages.success(request, 'Cuenta registrada')
        return render(request,"Recetas/Vista_de_Usuario.html",contexto)


        






def aamate(request):
    return render(request,'Recetas/aamate.html')

def index(request):
    return render(request,'Recetas/index.html')




def registrarse(request):
    return render(request,'Recetas/registrarse.html')

def recetas(request,id):
    receta1 = Receta.objects.get(idReceta=id)
    nacionalidad1 = Nacionalidad.objects.all()
    usuario1 = Usuario.objects.all()

    contexto = {
        "receta":receta1,
        "nacionalidad":nacionalidad1,
        "usuario":usuario1
    }
    
    return render(request,'Recetas/recetas.html',contexto)

def modificar_receta(request,id,sesi):
    sesion = Usuario.objects.get(idUsuario=sesi)
    receta1 = Receta.objects.get(idReceta=id)
    nacionalidad1 = Nacionalidad.objects.all()
    usuario1 = Usuario.objects.all()

    contexto = {
        "sesion":sesion,
        "receta":receta1,
        "nacionalidad":nacionalidad1,
        "usuario":usuario1
    }
    
    
    return render(request,'Recetas/modificar_receta.html',contexto)

def Ver_Receta_Usuario(request,id):
    sesion = Usuario.objects.get(idUsuario=id)
    recetas = Receta.objects.all()
    contexto={
        "recetas": recetas,
        "sesion":sesion
    }
    return render(request,'Recetas/Ver_Receta_Usuario.html',contexto)

def Ver_Receta_Admin(request,id):
    
    sesion = Usuario.objects.get(idUsuario=id)
    RecetasAdmin = Receta.objects.all()
    contexto={
        "RecetasAdmin": RecetasAdmin,
        "sesion":sesion
    }
    return render(request,'Recetas/Ver_Receta_Admin.html', contexto)


def Ver_Comen_Admin(request,id):
    sesion = Usuario.objects.get(idUsuario= id)
    comen = Comentario.objects.all()
    contexto = {
        "sesion":sesion,
        "comen":comen
        }
    return render(request,'Recetas/Ver_Comen_Admin.html',contexto)


def Menu_Recetas(request):
    RecetasChile = Receta.objects.all()
    return render(request,'Recetas/Menu_Recetas.html', {"RecetasChile": RecetasChile})


def Editar_Recetas_Admin(request,id):
    receta1 = Receta.objects.get(idReceta=id)
    nacionalidad1 = Nacionalidad.objects.all()
    usuario1 = Usuario.objects.all()

    contexto = {
        "receta":receta1,
        "nacionalidad":nacionalidad1,
        "usuario":usuario1
    }

    return render(request,'Recetas/Editar_Recetas_Admin.html',contexto)

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

def registrarse(request):
    return render(request,'Recetas/registrarse.html')



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



def listadoRecetas(request):
    receta = Receta.objects.all()
    contexto = {"lista_m":receta}
    return render(request,"Recetas/Creacion_Recetas.html",contexto)





def listadoUsuario(request):
    usuario = Usuario.objects.all()
    contexto = {"lista_u":usuario}
    return render(request,"Recetas/Ver_Usuario_Admin.html", contexto)

def listadoComentario(request):
    comen = Comentario.objects.all()
    contexto = {"lista_a":comen}
    return render(request,"Recetas/Ver_Comen_Admin.html", contexto)

def eliminar_comentario(request,id):
    usuar = Comentario.objects.get(idComentario = id)
    usuar.delete() #Elimina registro
    messages.success(request,'Comentario Eliminado')

    return redirect('Ver_Comen_Admin')

def eliminar_usuario(request,id):
    usuar = Usuario.objects.get(idUsuario = id)
    usuar.delete() #Elimina registro
    messages.success(request,'Usuario Eliminado')

    return redirect('Ver_Usuario_Admin')

def eliminar_receta(request,id,sesi):
    rec = Receta.objects.get(idReceta = id)
    rec.delete() #Elimina registro
    messages.success(request,'Receta Eliminada')

    sesion = Usuario.objects.get(idUsuario=sesi)
    rol2 = RolUsuario.objects.get(nomRol = 'Administrador')

    if sesion.RolUsuario.nomRol == rol2.nomRol:
        contexto ={"sesion":sesion}
        return render(request, 'Recetas/Ver_Receta_Admin.html',contexto)
    else:
        contexto ={"sesion":sesion}
        return render(request, 'Recetas/Ver_Receta_Usuario.html')

def modificar_receta_admin(request,id):
    receta1 = Receta.objects.get(idReceta = id)
    Nacio1 = Nacionalidad.objects.all()
    
    contexto = {
        "receta" :receta1,
        'nacionalidades' : Nacio1

    }
    return render(request,'Recetas/Editar_Recetas_Admin.html',contexto)

def modificar(request):
    iden      = request.POST['identificador']
    autor     = request.POST['autor']   
    imagen2   = request.FILES['imagen']
    nom_r     = request.POST['nomreceta']
    tiempo_r  = request.POST['tiempo']
    idNacio_r = request.POST['idNacio']
    ingre_r   = request.POST['ingredientes']
    prepa_r   = request.POST['preparacion']

    receta = Receta.objects.get(idReceta = iden)

    receta.nomReceta = nom_r
    receta.ingrediente = ingre_r
    receta.preparacion = prepa_r
    receta.tiempo = tiempo_r
    receta.fotoReceta = imagen2
    
    idNacio_r2 = Nacionalidad.objects.get(idNacionalidad = idNacio_r)

    receta.Nacionalidad = idNacio_r2
    receta.save() #update
    

    #messages.succes(request, 'Receta modificada')
    sesion = Usuario.objects.get(idUsuario=autor)

    rol2 = RolUsuario.objects.get(nomRol = 'Administrador')

    if sesion.RolUsuario.nomRol == rol2.nomRol:
        contexto ={"sesion":sesion}
        return render(request, 'Recetas/inicioAdmin.html',contexto)
    else:
        contexto ={"sesion":sesion}
        return render(request, 'Recetas/inicioUser.html',contexto)

    return redirect('Ver_Receta_Admin')

def registrarComentario(request):
    nomComen     = request.POST['nomComentario1']
    correo       = request.POST['emailComentario1']
    mensa        = request.POST['Mensaje1']

    Comentario.objects.create(nomComentario = nomComen, emailComentario = correo, Mensaje = mensa)

    messages.success(request, 'Mensaje Enviado')

    return redirect('contact')