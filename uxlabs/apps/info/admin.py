from django.contrib import admin
from . import models


@admin.register(models.SeccionNosotros)
class  SeccionNosotrosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'position']
