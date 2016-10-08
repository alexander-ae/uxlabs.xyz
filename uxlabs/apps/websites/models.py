from datetime import date

from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager
from colorfield.fields import ColorField

from apps.core.models import PositionModel, SlugModel


class Categoria(models.Model):
    nombre = models.CharField('Categoría', max_length=64)

    def __str__(self):
        return self.nombre


class Web(SlugModel):
    categoria = models.ManyToManyField(Categoria)
    resumen = models.TextField('Resumen', blank=True)
    detalle = models.TextField('Detalle', blank=True)
    enlace = models.URLField('Enlace', blank=True)
    fecha_de_revision = models.DateField('Fecha de revisión', blank=True, default=date.today)
    etiquetas = TaggableManager()

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('websites:detalle', kwargs={'slug': self.slug})


class WebImagen(models.Model):
    web = models.ForeignKey(Web, related_name='galeria')
    titulo = models.CharField('Título', max_length=64)
    imagen = models.ImageField('Imagen', upload_to='galeria')

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Galería'

    def __str__(self):
        return self.titulo


class WebColor(PositionModel):
    web = models.ForeignKey(Web, related_name='paleta_de_colores')
    color = ColorField(default='#FFFFFF')

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Paleta de colores'

    def __unicode__(self):
        return self.color
