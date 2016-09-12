from django.db import models
from uuslug import uuslug


class PositionModel(models.Model):
    position = models.SmallIntegerField('Posición', default=0)

    class Meta:
        abstract = True
        ordering = ['position']


class SlugModel(models.Model):
    nombre = models.CharField('Nombre', max_length=64)
    slug = models.SlugField('slug', max_length=64, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.nombre, instance=self)
        super(SlugModel, self).save(*args, **kwargs)
