from django.shortcuts import render, redirect
from .models import Venta
# Create your views here.
def ventas(request):
    lasventas = Venta.objects.all()
    return render(request, 'gestionarVentas.html', {"misventas": lasventas})

def registrarVenta(request):
    id = request.POST["txtid"]
    fechaventa = request.POST["datefechaventa"]
    idcliente = request.POST["txtidcliente"]
    idempleado = request.POST["txtidempleado"]
    listaproducto = request.POST["txtlistaproducto"]
    totalventa = request.POST["numtotalventa"]

    guardarVenta = Venta.objects.create(
        id = id,
        fechaventa = fechaventa,
        idcliente = idcliente,
        idempleado = idempleado,
        listaproducto = listaproducto,
        totalventa = totalventa
    ) 
    return redirect("ventas")

def seleccionarVenta(request, id):
    venta = Venta.objects.get(id=id)
    return render(request, "editarVentas.html", {"misventas": venta})

def editarVenta(request):
    id = request.POST["txtid"]
    fechaventa = request.POST["datefechaventa"]
    idcliente = request.POST["txtidcliente"]
    idempleado = request.POST["txtidempleado"]
    listaproducto = request.POST["txtlistaproducto"]
    totalventa = request.POST["numtotalventa"]
    venta = Venta.objects.get(id=id)
    venta.fechaventa = fechaventa
    venta.idcliente = idcliente
    venta.idempleado = idempleado
    venta.listaproducto = listaproducto
    venta.totalventa = totalventa

    venta.save()
    return redirect("ventas")

def borrarVenta(request, id):
    venta = Venta.objects.get(id=id)
    venta.delete()
    return redirect("ventas")
