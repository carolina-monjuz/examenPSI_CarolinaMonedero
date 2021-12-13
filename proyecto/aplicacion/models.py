from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.
class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=50)
    fechaAlta = models.DateField(null=True)

    def __str__(self):
        return self.nombreCliente    


class Habitacion(models.Model):
    numeroCamas = models.IntegerField(help_text="Numero entre 1 y 4")
    situacion = models.CharField(max_length=100)

    def __str__(self):
        return self.situacion + " " + str(self.numeroCamas)

class Ocupacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=CASCADE, null=True)
    habitacion = models.ForeignKey(Habitacion, on_delete=CASCADE, null=True)
    fechaEntrada = models.DateField(null=True)
    fechaSalida = models.DateField(null=True)

    def __str__(self):
        return self.cliente.__str__() + self.habitacion.__str__()
