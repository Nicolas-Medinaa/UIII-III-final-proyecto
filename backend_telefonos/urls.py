"""
URL configuration for backend_telefonos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('celular_app.urls')),
    path('clientes_app/',include('clientes_app.urls')),
    path('empleado_app/',include('empleado_app.urls')),
    path('inventario_app/',include('inventario_app.urls')),
    path('proveedor_app/',include('proveedor_app.urls')),
    path('venta_app/',include('venta_app.urls')),

]
