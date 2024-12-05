from django.urls import path
from proveedor_app import views

urlpatterns = [
    path("proveedores",views.proveedores,name="proveedores"),
    path("registrarProveedor/",views.registrarProveedor,name="registrarProveedor"),
    path("seleccionarProveedor/<id>",views.seleccionarProveedor,name="seleccionarProveedor"),
    path("editarProveedor/",views.editarProveedor, name="editarProveedor"),
    path("borrarProveedor/<id>",views.borrarProveedor,name="borrarProveedor"),
    
]