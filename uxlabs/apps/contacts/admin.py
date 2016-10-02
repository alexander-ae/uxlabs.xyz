from django.contrib import admin
from . import models


@admin.register(models.Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'email', 'fecha', 'estado')
    readonly_fields = ('fecha', 'nombres', 'email', 'asunto', 'detalle')
    search_fields = ('nombres', 'email', 'asunto')
    ordering = ('-fecha',)
    list_per_page = 50
