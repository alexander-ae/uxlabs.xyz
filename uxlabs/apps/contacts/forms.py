from django import forms
from . import models


class ContactoForm(forms.ModelForm):

    class Meta:
        model = models.Contacto
        fields = ('nombres', 'email', 'asunto', 'detalle')
