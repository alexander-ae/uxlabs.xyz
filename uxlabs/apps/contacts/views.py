from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ContactoForm
from .models import Contacto


def contacto(request):

    if request.method == 'POST':
        form = ContactoForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = ContactoForm()
    return render(request, 'contacts/contacto.html', locals())
