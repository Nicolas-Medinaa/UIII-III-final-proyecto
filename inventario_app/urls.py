from django.urls import path
from inventario_app import views

urlpatterns = [
    path("inventarios",views.inventarios,name="inventarios"),
    path("registrarInventario/",views.registrarInventario,name="registrarInventario"),
    path("seleccionarInventario/<id>",views.seleccionarInventario,name="seleccionarInventario"),
    path("editarInventario/",views.editarInventario, name="editarInventario"),
    path("borrarInventario/<id>",views.borrarInventario,name="borrarInventario"),
    
]