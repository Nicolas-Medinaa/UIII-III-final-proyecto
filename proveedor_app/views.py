from django.shortcuts import render, redirect
from .models import Proveedor
# Create your views here.
def proveedores(request):
    losproveedores = Proveedor.objects.all()
    return render(request, 'gestionarProveedores.html', {"misproveedores": losproveedores})

def registrarProveedor(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["numtelefono"]
    correoelectronico = request.POST["txtcorreoelectronico"]
    direccion = request.POST["txtdireccion"]
    listasproductos = request.POST["txtlistasproductos"]
    edad = request.POST["numedad"]

    guardarProveedor = Proveedor.objects.create(
        id = id,
        nombre = nombre,
        telefono = telefono,
        correoelectronico = correoelectronico,
        direccion = direccion,
        listasproductos = listasproductos,
        edad = edad,
    ) 
    return redirect("proveedores")

def seleccionarProveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    return render(request, "editarProveedores.html", {"misproveedores": proveedor})

def editarProveedor(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["numtelefono"]
    correoelectronico = request.POST["txtcorreoelectronico"]
    direccion = request.POST["txtdireccion"]
    listasproductos = request.POST["txtlistasproductos"]
    edad = request.POST["numedad"]
    proveedor = Proveedor.objects.get(id=id)
    proveedor.nombre = nombre
    proveedor.telefono = telefono
    proveedor.correoelectronico = correoelectronico
    proveedor.direccion = direccion
    proveedor.listasproductos = listasproductos
    proveedor.edad = edad

    proveedor.save()
    return redirect("proveedores")

def borrarProveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    return redirect("proveedores")
