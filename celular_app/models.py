from django.db import models

# Create your models here.
class Celular(models.Model):
    id=models.IntegerField(primary_key=True)
    marca=models.CharField(max_length=10)
    modelo=models.CharField(max_length=10)
    gama=models.CharField(max_length=10) 
    precios=models.IntegerField()
    idproveedor=models.IntegerField()
    idinventario=models.IntegerField()



    def __str__(self) -> str:
        return self.marca
