from django.db import models

# Create your models here.
class Cliente(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    correo=models.CharField(max_length=20)
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=20) 
    historial=models.TextField(max_length=400)
    idinventario=models.IntegerField()



    def __str__(self) -> str:
        return self.nombre
