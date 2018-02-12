# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Catalogo(models.Model):
    nombre = models.CharField(max_length=45, null=False, blank=False)
    estado = models.BooleanField(default=False, null=False)
    descripcion = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class ItemCatalogo(models.Model):
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=45, null=False, blank=False)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    identificacion = models.CharField(max_length=30, null=False, blank=False, unique=True)
    nombres = models.CharField(max_length=60, null=False, blank=False)
    apellidos = models.CharField(max_length=60, null=False, blank=False)
    direccion = models.CharField(max_length=60)
    numeroCelular = models.CharField(max_length=10)
    numeroTelefono = models.CharField(max_length=7)
    email = models.EmailField(max_length=254)
    fotografia = models.ImageField(upload_to = '../imagenes/empleados/')
    cargo = models.ManyToManyField(ItemCatalogo)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)

class Vehiculo(models.Model):
    #marca = models.CharField(max_length=30, null=False, blank=False)
    marca = models.ForeignKey(ItemCatalogo, on_delete=models.CASCADE, related_name='marcaVehiculo')
    placas = models.CharField(max_length=7, null=False, blank=False, unique=True)
    chasis = models.CharField(max_length=30, null=False, blank=False, unique=True)
    fotografia = models.ImageField(upload_to = '../imagenes/catalogoVehiculos/')
    caracteristicas = models.ManyToManyField(ItemCatalogo, related_name='caracteristicasVehiculo')

    def __str__(self):
        return '{} {} {}'.format(self.marca, self.placas, self.chasis)

class Cliente(models.Model):
    identificacion = models.CharField(max_length=30, null=False, blank=False, unique=True)
    nombres = models.CharField(max_length=60, null=False, blank=False)
    apellidos = models.CharField(max_length=60, null=False, blank=False)
    direccion = models.CharField(max_length=60)
    numeroCelular = models.CharField(max_length=10)
    numeroTelefono = models.CharField(max_length=7)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)

class Reserva(models.Model):
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.fechaInicio, self.fechaFin, self.vehiculo)
