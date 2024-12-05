from django.urls import path
from empleado_app import views

urlpatterns = [
    path("empleados",views.empleados,name="empleados"),
    path("registrarEmpleado/",views.registrarEmpleado,name="registrarEmpleado"),
    path("seleccionarEmpleado/<id>",views.seleccionarEmpleado,name="seleccionarEmpleado"),
    path("editarEmpleado/",views.editarEmpleado, name="editarEmpleado"),
    path("borrarEmpleado/<id>",views.borrarEmpleado,name="borrarEmpleado"),
    
]