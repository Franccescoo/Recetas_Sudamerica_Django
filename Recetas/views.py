from django.shortcuts import render

# Create your views here.
    

def listado(request):
    mascotas = Mascota.objects.all()
    contexto = {"lista_m":mascotas}
    return render(request,"Ventas/listadoM.html", contexto)

def formulario(request):
    razas = Raza.objects.all()
    contexto = {"lista_r": razas}
    return render(request,"Ventas/formulario.html",contexto)

def registrar(request):
    chip2 = request.POST['chip1']
    nombre2 = request.POST['nombre1']
    edad2 = request.POST['edad1']
    color2 = request.POST['color1']
    raza2 = request.POST['raza1']
    foto2 = request.FILES['foto1']

    raza3 = Raza.objects.get(idRaza = raza2)
    Mascota.objects.create(chip = chip2, nombreMascota = nombre2, edad = edad2, colorPelo = color2, foto = foto2, raza = raza3)
    return redirect('formulario')

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

def Vista_deVista_de_UsuarioAdmin(request):
    return render(request,'Recetas/Vista_de_Usuario.html')
