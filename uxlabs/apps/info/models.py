from django.db import models

from apps.core.models import PositionModel


class SeccionNosotros(PositionModel):
    titulo = models.CharField('Título', max_length=64)
    detalle = models.TextField('Detalle')

    class Meta:
        verbose_name = 'Bloque de sección Nosotros'
        verbose_name_plural = 'Sección Nosotros'
        ordering = ['position']

    def __str__(self):
        return self.titulo
