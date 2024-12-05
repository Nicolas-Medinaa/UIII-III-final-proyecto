from django.urls import path
from celular_app import views

urlpatterns = [
    path("",views.celular,name="celular"),
    path("registrarCelular/",views.registrarCelular,name="registrarCelular"),
    path("seleccionarCelular/<id>",views.seleccionarCelular,name="seleccionarCelular"),
    path("editarCelular/",views.editarCelular, name="editarCelular"),
    path("borrarCelular/<id>",views.borrarCelular,name="borrarCelular"),
    
]