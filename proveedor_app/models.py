from django.db import models


# Create your models here.
class Proveedor(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=20) 
    telefono=models.IntegerField()
    correoelectronico=models.CharField(max_length=20) 
    direccion=models.CharField(max_length=50) 
    listasproductos=models.TextField(max_length=500)
    edad=models.SmallIntegerField()
    





    def __str__(self) -> str:
        return self.id
