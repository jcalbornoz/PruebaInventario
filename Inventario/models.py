from django.db import models

# Create your models here.
class Inventario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=40) 
    descripcion = models.CharField(max_length=400)
    tipo = models.CharField(max_length=400)
    serial = models.CharField(max_length=40) 
    valorcompra = models.DecimalField(max_digits=18,decimal_places=2)
    fechadecompra = models.DateField()
    area = models.CharField(max_length=50) 
    persona = models.CharField(max_length=50) 
    class Meta:
      db_table = "Inventario"


class Tipo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=40) 
    descripcion = models.CharField(max_length=400)
   
    class Meta:
      db_table = "Tipo"
      
class Area(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=40) 
    descripcion = models.CharField(max_length=400)
   
    class Meta:
      db_table = "Area"

class Persona(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50) 
    fechaNacimiento = models.DateField()
    area=models.Lookup()
    class Meta:
      db_table = "Persona"

  
class Estado(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=40) 
    descripcion = models.CharField(max_length=400)
   
    class Meta:
      db_table = "Estado"