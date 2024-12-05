from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.
def clientes(request):
    losclientes=Cliente.objects.all()
    return render(request,'gestionarClientes.html',{"misclientes":losclientes})

def registrarCliente(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    correo = request.POST["txtcorreo"]
    telefono = request.POST["numtelefono"]
    direccion = request.POST["txtdireccion"]
    historial = request.POST["txthistorial"]
    idinventario = request.POST["numinventario"]


   



    guardarCliente=Cliente.objects.create(
        id=id,
        nombre=nombre,
        apellido=apellido,
        correo=correo,
        telefono=telefono,
        direccion=direccion,
        historial=historial,
        idinventario=idinventario
    ) 
    return redirect ("clientes")

def seleccionarCliente(request,id):
    cliente=Cliente.objects.get(id=id)
    return render(request,"editarClientes.html",{"misclientes":cliente})


def editarCliente(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    correo = request.POST["txtcorreo"]
    telefono = request.POST["numtelefono"]
    direccion = request.POST["txtdireccion"]
    historial = request.POST["txthistorial"]
    idinventario = request.POST["numinventario"]
    cliente=Cliente.objects.get(id=id)
    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.correo=correo
    cliente.telefono=telefono
    cliente.direccion=direccion
    cliente.historial=historial
    cliente.idinventario=idinventario

   
    cliente.save()
    return redirect("clientes") #dsf


def borrarCliente(request,id):
    cliente=Cliente.objects.get(id=id)
    cliente.delete()
    return redirect("clientes") #asdsda
