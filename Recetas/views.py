from django.shortcuts import render

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

    