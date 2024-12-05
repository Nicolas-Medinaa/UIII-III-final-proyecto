from django.db import models

# Create your models here.
class Inventario(models.Model):
    id=models.IntegerField(primary_key=True)
    marca=models.CharField(max_length=50) 
    modelo=models.CharField(max_length=20)
    cantidad=models.SmallIntegerField()
    año=models.IntegerField()
    idproveedor=models.IntegerField()
    sucursal=models.IntegerField() 





    def __str__(self) -> str:
        return self.id
