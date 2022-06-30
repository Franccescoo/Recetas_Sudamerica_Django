from ast import alias
from asyncio.windows_events import NULL
from email import message
from tkinter.tix import Tree
from django.shortcuts import render, redirect
from .models import Favorito,Usuario,Receta,Nacionalidad,RolUsuario,Comentario,Valoracion,Dieta,Alimento
from django.contrib import messages
# Create your views here.

def registrarFavorito(request,id,sesi):
    usu        = Usuario.objects.get(idUsuario=sesi)
    rece       = Receta.objects.get(idReceta=id)
    Favorito.objects.create(Usuario = usu, Receta = rece)

    return redirect('recetasSesion',sesi,id)

def eliminarFavorito(request,id,sesi):
    usu        = Usuario.objects.get(idUsuario=sesi)
    rece       = Receta.objects.get(idReceta=id)

    favo = Favorito.objects.get(Usuario = usu, Receta = rece)
    favo.delete() #Elimina registro
    return redirect('recetasSesion',sesi,id)


def MisFavoritos(request,id):
    sesion = Usuario.objects.get(idUsuario=id)
    favorito = Favorito.objects.all()
    contexto={
        "recetas": favorito,
        "sesion": sesion
    }
    return render(request,'Recetas/MisFavoritos.html',contexto)

def modificarFotoUser(request,id):
    sesion = Usuario.objects.get(idUsuario = id)

    contexto = {
        "sesion":sesion
    }

    return render(request,'Recetas/modificarFotoUser.html',contexto)

def fotoUserModificada(request,id):
    
    usuario = Usuario.objects.get(idUsuario=id)
    foto2 = request.FILES['fot']
      
    usuario.foto = foto2
    usuario.save() #update
    
    return redirect ('modificarFotoUser',id)

def modificar_receta(request,id,sesi):
    sesion = Usuario.objects.get(idUsuario=sesi)
    receta1 = Receta.objects.get(idReceta=id)
    nacionalidad1 = Nacionalidad.objects.all()
    usuario1 = Usuario.objects.all()
    alias3           = Alimento.objects.all()
    ali3             = Dieta.objects.all()

    contexto = {
        "sesion":sesion,
        "receta":receta1,
        "nacionalidad":nacionalidad1,
        "usuario":usuario1,
        "alim": alias3,
        "diets": ali3
    }
    return render(request,'Recetas/modificar_receta.html',contexto)


def modificar(request,id,sesi):
    receta = Receta.objects.get(idReceta = id)
    
    nom_r     = request.POST['nomreceta']
    tiempo_r  = request.POST['tiempo']
    idNacio_r = request.POST['idNacio']
    ingre_r   = request.POST['ingredientes']
    prepa_r   = request.POST['preparacion']
    alias     = request.POST['idAli']
    dietas    = request.POST['idDiet']
    

    receta.nomReceta = nom_r
    receta.ingrediente = ingre_r
    receta.preparacion = prepa_r
    receta.tiempo = tiempo_r

    try:
        imagen2   = request.FILES['imagen']
        receta.fotoReceta = imagen2
    except:
        imagen2 = NULL

    idNacio_r2  = Nacionalidad.objects.get(idNacionalidad = idNacio_r)
    dietas2     = Dieta.objects.get(idDieta = dietas)
    alias2      = Alimento.objects.get(idAlimento = alias)

    receta.Nacionalidad = idNacio_r2
    receta.Dieta = dietas2
    receta.Alimento = alias2
    receta.save() #update
    

    #messages.succes(request, 'Receta modificada')

    return redirect ('modificar_receta',receta.idReceta,sesi)
   

def modificarContra(request,id):
    sesion = Usuario.objects.get(idUsuario = id)

    contexto = {
        "sesion":sesion
    }

    return render(request,'Recetas/ModificarContra.html',contexto)


def contraModificado(request,id):
    
    contrasena2       = request.POST['pass1'] 

    usuario = Usuario.objects.get(idUsuario=id)
      

    usuario.contrasena = contrasena2
    usuario.save() #update
    return redirect ('modificarContra',id)







def registrarRecetas(request,id):
    try:
        imagen2          = request.FILES['imagen']
    except:
        imagen2="../../static/Recetas/img/Token/foto_default_receta.png"
    nomreceta2       = request.POST['nomreceta']
    tiempo2          = request.POST['tiempo']
    idNacionalidad2  = request.POST['idNacio']
    ingredientes2    = request.POST['ingredientes']
    preparacion2     = request.POST['preparacion']
    alias            = request.POST['idAli']
    dietas           = request.POST['idDiet']

    Nacionalidad3    = Nacionalidad.objects.get(idNacionalidad = idNacionalidad2)
    alias3           = Alimento.objects.get(idAlimento = alias)
    ali3             = Dieta.objects.get(idDieta = dietas)
    Usuario3         = Usuario.objects.get(idUsuario = id)

    Receta.objects.create(Usuario=Usuario3,fotoReceta =imagen2, nomReceta =nomreceta2, ingrediente =ingredientes2, preparacion=preparacion2, tiempo=tiempo2, Nacionalidad=Nacionalidad3, Alimento = alias3, Dieta = ali3)
    
    messages.success(request, 'Receta Registrada')

    return redirect ('Creacion_Recetas',id)


def Creacion_Recetas(request,id):
    sesion = Usuario.objects.get(idUsuario=id)
    Nacio = Nacionalidad.objects.all()
    ali = Alimento.objects.all()
    diet = Dieta.objects.all()
    contexto = {
        "sesion":sesion,
        "lista_r":Nacio,
        "lista_a":ali,
        "lista_d":diet}
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
            return redirect ('Vista_de_Admin',x.idUsuario)
        else:
            return redirect ('Vista_de_Usuario',x.idUsuario)

    except Usuario.DoesNotExist:
        # messages.error(request, 'Usuario y/o clave incorrecta')
        return redirect ('Login')


def inicioAdmin(request,sesion):

    contexto={
        "sesion":sesion
    }
    return render(request,'Recetas/inicioAdmin.html',contexto)
def inicioUser(request,sesion):

    contexto={
        "sesion":sesion
    }
    return render(request,'Recetas/inicioUser.html',contexto)



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
    try:
        foto2       = request.FILES['foto1']
    except:
        foto2 = "../../static/Recetas/img/Token/pngwing.com.png"
    email2      = request.POST['email']
    contra2     = request.POST['password1']
    try:
        c = Usuario.objects.get(email = email2)
        c1 = False
    except Usuario.DoesNotExist:
        c1 = True      
    try:
        x = Usuario.objects.get(username = nick)
        x1 = False
    except Usuario.DoesNotExist:
        x1 = True
    if c1 == True and x1 == True:
        messages.error(request, 'Cargando')
        Usuario.objects.create(nomUsuario = nombre2, apellidoCompleto = apellido2, username = nick, email = email2, foto = foto2, contrasena = contra2)
        sesion = Usuario.objects.get(username=nick)
        contexto ={
        "sesion":sesion
        }
        messages.success(request, 'Cuenta registrada')
        return redirect ('Vista_de_Usuario',sesion.idUsuario)
    else:
        messages.error(request, 'El nombre de usuario o correo ya estan ocupados')
        return redirect ('registrarse')


def modificarPerfil(request,id):
    sesion = Usuario.objects.get(idUsuario = id)

    contexto = {
        "sesion":sesion
    }

    return render(request,'Recetas/ModificarPerfil.html',contexto)

def perfilModificado(request,id):
    idUsuario2        = id
    usuario           = Usuario.objects.get(idUsuario = idUsuario2)
    nomUsuario2       = request.POST['nomUser']
    apellidoCompleto2 = request.POST['apeUser']
    email2            = request.POST['email']

    try:
        c = Usuario.objects.get(email = email2)
        if idUsuario2 == c.idUsuario:
            c1 = True
        else:
            c1 = False
    except Usuario.DoesNotExist:
        c1 = True
    


    if c1 == True :
        messages.error(request, 'Perfil modificado')
        usuario.nomUsuario = nomUsuario2
        usuario.apellidoCompleto = apellidoCompleto2
        usuario.email = email2
        usuario.save() #update
        return redirect ('modificarPerfil',id)
    else:
        messages.error(request, 'El nombre de usuario o correo ya estan ocupados')
        return redirect ('modificarPerfil',id)


        
            

        



def aamate(request):
    return render(request,'Recetas/aamate.html')

def index(request):
    sesion = Usuario.objects.get(idUsuario=id)
    contexto={
        "sesion":sesion
    }
    return render(request,'Recetas/index.html', contexto)

def Menu_RecetasSesion(request,idUser):
    sesion = Usuario.objects.get(idUsuario=idUser)
    RecetasChile = Receta.objects.all()
    contexto={
        "RecetasChile": RecetasChile,
        "sesion" : sesion

    }
    return render(request,'Recetas/Menu_RecetasSesion.html', contexto)

def recetasSesion(request, idUser ,idRec):
    sesion = Usuario.objects.get(idUsuario=idUser)
    receta1 = Receta.objects.get(idReceta=idRec)
    nacionalidad1 = Nacionalidad.objects.all()
    usuario1 = Usuario.objects.all()
    valo = Valoracion.objects.all()
    try:
        favo = Favorito.objects.get(Usuario = sesion, Receta = receta1)
    except:
        favo = NULL
    contexto = {
        "receta":receta1,
        "nacionalidad":nacionalidad1,
        "usuario":usuario1,
        "valo":valo,
        "sesion" : sesion,
        "favorito": favo,
    }
    return render(request,'Recetas/recetasSesion.html',contexto)

def indexSesion(request, idUser):
    sesion = Usuario.objects.get(idUsuario=idUser)

    contexto = {
        "sesion" : sesion
    }
    return render(request,'Recetas/indexSesion.html',contexto)

def contactSesion(request, idUser):
    sesion = Usuario.objects.get(idUsuario=idUser)

    contexto = {
        "sesion" : sesion
    }
    return render(request,'Recetas/contactSesion.html',contexto)


def recetas(request,id):
    receta1 = Receta.objects.get(idReceta=id)
    nacionalidad1 = Nacionalidad.objects.all()
    usuario1 = Usuario.objects.all()
    valo = Valoracion.objects.all()

    contexto = {
        "receta":receta1,
        "nacionalidad":nacionalidad1,
        "usuario":usuario1,
        "valo":valo
    }
    
    return render(request,'Recetas/recetas.html',contexto)



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
        "comentario":comen
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

def listadoValoracion(request):
    comen = Valoracion.objects.all()
    contexto = {"lista_a":comen}
    return render(request,"Recetas/plantillaNueva.html", contexto)

def eliminar_comentario(request,id,sesi):
    usuar = Comentario.objects.get(idComentario = id)
    usuar.delete() #Elimina registro
    messages.success(request,'Comentario Eliminado')

    x = Usuario.objects.get(idUsuario=sesi)
    rol2 = RolUsuario.objects.get(nomRol = 'Administrador')

    if x.RolUsuario.nomRol == rol2.nomRol:
        return redirect ('Ver_Comen_Admin',sesi)
    else:
        return redirect ('Ver_Comen_Admin',sesi)



def eliminar_usuario(request,id,sesi):
    usuar = Usuario.objects.get(idUsuario = id)
    usuar.delete() #Elimina registro
    messages.success(request,'Usuario Eliminado')

    x = Usuario.objects.get(idUsuario=sesi)
    rol2 = RolUsuario.objects.get(nomRol = 'Administrador')

    if x.RolUsuario.nomRol == rol2.nomRol:
        return redirect ('Ver_Usuario_Admin',sesi)
    else:
        return redirect ('Ver_Usuario_Admin',sesi)

def eliminar_receta(request,id,sesi):
    rec = Receta.objects.get(idReceta = id)
    rec.delete() #Elimina registro
    messages.success(request,'Receta Eliminada')

    sesion = Usuario.objects.get(idUsuario=sesi)

    rol2 = RolUsuario.objects.get(nomRol = 'Administrador')

    if sesion.RolUsuario.nomRol == rol2.nomRol:
        return redirect ('Ver_Receta_Admin',sesi)
    else:
        return redirect ('Ver_Receta_Usuario',sesi)

def modificar_receta_admin(request,id):
    receta1          = Receta.objects.get(idReceta = id)
    Nacio1           = Nacionalidad.objects.all()
    alias3           = Alimento.objects.all()
    ali3             = Dieta.objects.all()
    
    contexto = {
        "receta" :receta1,
        'nacionalidades' : Nacio1,
        'alim': alias3,
        'diets': ali3
        

    }
    return render(request,'Recetas/Editar_Recetas_Admin.html',contexto)




def registrarComentarioSesion(request,id):
    nomComen     = request.POST['nomComentario1']
    correo       = request.POST['emailComentario1']
    mensa        = request.POST['Mensaje1']

    Comentario.objects.create(nomComentario = nomComen, emailComentario = correo, Mensaje = mensa)

    messages.success(request, 'Mensaje Enviado')

    return redirect('contactSesion',id)
   

def registrarComentario(request):
    nomComen     = request.POST['nomComentario1']
    correo       = request.POST['emailComentario1']
    mensa        = request.POST['Mensaje1']

    Comentario.objects.create(nomComentario = nomComen, emailComentario = correo, Mensaje = mensa)

    messages.success(request, 'Mensaje Enviado')

    return redirect('contact')


def registrarValoracion(request,idUser,idRec):
    user         = Usuario.objects.get(idUsuario=idUser)
    Rece         = Receta.objects.get(idReceta=idRec)
    mensa        = request.POST['Mensaje1']
    valo         = request.POST['estrellas']
    

    Valoracion.objects.create(Usuario = user ,Receta = Rece ,mensajeValoracion = mensa, estrellaValoracion = valo)

    messages.success(request, 'Valoracion Enviada')

    return redirect('recetasSesion',idUser,idRec)