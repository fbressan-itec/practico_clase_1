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

    #para que se lea mejor en panel de admin
    def __str__(self):
        return f"{self.marca} {(self.patente)}"


class Spot (models.Model):

    ESTADO_CHOICES= [
        ('LIBRE', "Libre"),
        ('OCUPADO', 'Ocupado')
    ]

    numero=models.IntegerField(verbose_name="Cochera N°", unique=True,)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='LIBRE', verbose_name="Estado Cochera")
    ingreso=models.DateTimeField(auto_now=True, verbose_name="Fecha de Entrada", blank=True, null=True)
    responsable=models.ForeignKey(User, default=None, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Empleado")
    vehiculo=models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f"Cochera N° {self.numero}"

#nuevo modelo cn fk
class Pago(models.Model):

    METODO_CHOICES = [
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
        ('TRANSFERENCIA', 'Transferencia')
    ]

    spot = models.ForeignKey(Spot, on_delete=models.PROTECT, verbose_name="Cochera")
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT, verbose_name="Vehiculo")
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto Cobrado")
    metodo_pago = models.CharField(max_length=20, choices=METODO_CHOICES, default='EFECTIVO', verbose_name="Metodo de Pago")
    fecha_pago = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del pago")

    def __str__(self):
        return f"Pago ${self.monto} - Cochera {self.spot.numero}"
