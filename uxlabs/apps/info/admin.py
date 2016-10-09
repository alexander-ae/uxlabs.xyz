from django.contrib import admin
from . import models


@admin.register(models.SeccionNosotros)
class  SeccionNosotrosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'position']


@admin.register(models.SeccionLegal)
class  SeccionLegalAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'position']
