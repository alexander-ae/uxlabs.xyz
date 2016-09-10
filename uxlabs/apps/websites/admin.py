from django.contrib import admin

from . import models


class ImagenInline(admin.TabularInline):
    model = models.WebImagen
    extra = 0


@admin.register(models.Web)
class WebAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_de_revision']
    inlines = [ImagenInline]


admin.site.register(models.Categoria)
