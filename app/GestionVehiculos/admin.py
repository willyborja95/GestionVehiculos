from django.contrib import admin
from GestionVehiculos import models
# Register your models here.


admin.site.register(models.Catalogo)
admin.site.register(models.ItemCatalogo)
admin.site.register(models.Empleado)
admin.site.register(models.Vehiculo)
admin.site.register(models.Cliente)
admin.site.register(models.Reserva)
