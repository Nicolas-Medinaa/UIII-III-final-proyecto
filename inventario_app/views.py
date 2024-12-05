from django.shortcuts import render, redirect
from .models import Inventario
# Create your views here.
def inventarios(request):
    losinventarios = Inventario.objects.all()
    return render(request, 'gestionarInventarios.html', {"misinventarios": losinventarios})

def registrarInventario(request):
    id = request.POST["txtid"]
    marca = request.POST["txtmarca"]
    modelo = request.POST["txtmodelo"]
    cantidad = request.POST["numcantidad"]
    año = request.POST["numaño"]
    idproveedor = request.POST["txtidproveedor"]
    sucursal = request.POST["txtsucursal"]

    guardarInventario = Inventario.objects.create(
        id = id,
        marca = marca,
        modelo = modelo,
        cantidad = cantidad,
        año = año,
        idproveedor = idproveedor,
        sucursal = sucursal
    ) 
    return redirect("inventarios")

def seleccionarInventario(request, id):
    inventario = Inventario.objects.get(id=id)
    return render(request, "editarInventarios.html", {"misinventarios": inventario})

def editarInventario(request):
    id = request.POST["txtid"]
    marca = request.POST["txtmarca"]
    modelo = request.POST["txtmodelo"]
    cantidad = request.POST["numcantidad"]
    año = request.POST["numaño"]
    idproveedor = request.POST["txtidproveedor"]
    sucursal = request.POST["txtsucursal"]
    inventario = Inventario.objects.get(id=id)
    inventario.marca = marca
    inventario.modelo = modelo
    inventario.cantidad = cantidad
    inventario.año = año
    inventario.idproveedor = idproveedor
    inventario.sucursal = sucursal

    inventario.save()
    return redirect("inventarios")

def borrarInventario(request, id):
    inventario = Inventario.objects.get(id=id)
    inventario.delete()
    return redirect("inventarios")
