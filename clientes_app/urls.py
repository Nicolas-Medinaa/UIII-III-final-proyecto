from django.urls import path
from clientes_app import views

urlpatterns = [
    path("clientes",views.clientes,name="clientes"),
    path("registrarCliente/",views.registrarCliente,name="registrarCliente"),
    path("seleccionarCliente/<id>",views.seleccionarCliente,name="seleccionarCliente"),
    path("editarCliente/",views.editarCliente, name="editarCliente"),
    path("borrarCliente/<id>",views.borrarCliente,name="borrarCliente"),
    
]