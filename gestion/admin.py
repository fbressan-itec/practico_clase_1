from django.contrib import admin
from .models import Vehiculo, Spot

# Register your models here.

@admin.register(Vehiculo)
class VehiculoAdmin (admin.ModelAdmin):
    list_display = ("marca", "tipo", "patente", "color")
    list_filter = ("patente", )
    search_fields = ("marca", )


@admin.register(Spot)
class SpotAdmin (admin.ModelAdmin):
    list_display = ("id", "numero", "entrada", "responsable", "vehiculo")
    list_filter =  ("numero", )
    search_fields = ("numero", )