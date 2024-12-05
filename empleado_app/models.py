from django.db import models

# Create your models here.
class Empleado(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    cargo=models.CharField(max_length=50)
    correoelectronico=models.CharField(max_length=50) 
    telefono=models.IntegerField() 
    fechacontratacion=models.DateField() 




    def __str__(self) -> str:
        return self.nombre
