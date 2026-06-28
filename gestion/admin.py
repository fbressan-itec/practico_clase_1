from django.contrib import admin
from .models import Vehiculo, Spot, Pago

# Register your models here.

@admin.register(Vehiculo)
class VehiculoAdmin (admin.ModelAdmin):
    list_display = ("marca", "tipo", "patente", "color")
    list_filter = ("patente", "tipo", "color" )
    search_fields = ("marca", "tipo")


@admin.register(Spot)
class SpotAdmin (admin.ModelAdmin):
    list_display = ("id", "numero", "estado", "ingreso", "responsable", "vehiculo")
    list_filter =  ("numero", "estado" )
    ordering = ("estado", )
    search_fields = ("numero", "vehiculo__patente", "vehiculo__marca", "estado" ) #para buscar relaciones se usa doble guion bajo __
    readonly_fields = ("ingreso",) #para que aparzca en formAdmin pero no se pueda editar

@admin.register(Pago)
class PagoAdmin (admin.ModelAdmin):
    list_display = ("spot", "vehiculo", "monto", "metodo_pago", "fecha_pago")
    list_filter = ("spot", )
    search_fields = ("spot__numero", "vehiculo__patente", "vehiculo__marca")