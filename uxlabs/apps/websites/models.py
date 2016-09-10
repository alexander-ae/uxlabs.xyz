from django.db import models
from datetime import date


class Categoria(models.Model):
    nombre = models.CharField('Categoría', max_length=64)

    def __str__(self):
        return self.nombre


class Web(models.Model):
    categoria = models.ManyToManyField(Categoria)
    nombre = models.CharField('Nombre', max_length=64)
    resumen = models.TextField('Resumen', blank=True)
    detalle = models.TextField('Detalle', blank=True)
    enlace = models.URLField('Enlace', blank=True)
    fecha_de_revision = models.DateField('Fecha de revisión', blank=True, default=date.today)

    def __str__(self):
        return self.nombre
