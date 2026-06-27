from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vehiculo (models.Model):
    # Elecciones fijas tipo vehiculo
    TIPO_CHOICES = [
        ('AUTO', 'Auto'),
        ('CAMIONETA', 'Camioneta'),
        ('OTRO', 'otro'),
    ]
    marca=models.CharField(max_length=50,)
    tipo=models.CharField(max_length=10, choices=TIPO_CHOICES, default='AUTO')
    patente=models.CharField(max_length=10,)
    color=models.CharField(max_length=50,)


class Spot (models.Model):
    numero=models.IntegerField(verbose_name="Cochera N°", unique=True)
    entrada=models.DateTimeField(auto_now=True, verbose_name="Fecha de Entrada")
    responsable=models.ForeignKey(User, default=None, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Empleado")
    vehiculo=models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, blank=True, null=True)