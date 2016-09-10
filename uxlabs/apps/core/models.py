from django.db import models


class PositionModel(models.Model):
    position = models.SmallIntegerField('Posición', default=0)

    class Meta:
        abstract = True
        ordering = ['position']
