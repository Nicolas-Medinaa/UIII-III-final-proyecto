from django.shortcuts import render, redirect
from .models import Celular
# Create your views here.
def celular(request):
    loscelulares=Celular.objects.all()
    return render(request,'gestionarCelulares.html',{"miscelulares":loscelulares})

def registrarCelular(request):
    id=request.POST["txtid"]
    marca=request.POST["txtmarca"]
    modelo=request.POST["txtmodelo"]
    gama=request.POST["txtgama"]
    precios=request.POST["numprecio"]
    idproveedor=request.POST["numidproveedor"]
    idinventario=request.POST["numidinventario"]

   



    guardarCelular=Celular.objects.create(
        id=id,
        marca=marca,
        modelo=modelo,
        gama=gama,
        precios=precios,
        idproveedor=idproveedor,
        idinventario=idinventario
        
    ) 
    return redirect ("/")

def seleccionarCelular(request,id):
    celular=Celular.objects.get(id=id)
    return render(request,"editarCelulares.html",{"miscelulares":celular})


def editarCelular(request):
    id=request.POST["txtid"]
    marca=request.POST["txtmarca"]
    modelo=request.POST["txtmodelo"]
    gama=request.POST["txtgama"]
    precios=request.POST["numprecio"]
    idproveedor=request.POST["numidproveedor"]
    idinventario=request.POST["numidinventario"]


    celular=Celular.objects.get(id=id)
    celular.marca=marca
    celular.modelo=modelo
    celular.gama=gama
    celular.precios=precios
    celular.idproveedor=idproveedor
    celular.idinventario=idinventario
   
    celular.save()
    return redirect("/") #dsf


def borrarCelular(request,id):
    celular=Celular.objects.get(id=id)
    celular.delete()
    return redirect("/") #asdsda
