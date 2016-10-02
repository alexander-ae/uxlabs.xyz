from datetime import datetime
from django.db import models
from . import choices

class Contacto(models.Model):
    fecha = models.DateTimeField('Fecha/Hora', default=datetime.now)
    estado = models.CharField('Estado', max_length=1, choices=choices.ESTADO_FORMULARIO_CONTACTO, default=choices.ESTADO_PENDIENTE)
    nombres = models.CharField('Nombres', max_length=32)
    email = models.EmailField('Email')
    asunto = models.CharField('Asunto', max_length=48)
    detalle = models.TextField('Detalle')

    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name = 'Formulario de Contacto'
        verbose_name_plural = 'Formularios de Contacto'
