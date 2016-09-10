from django.shortcuts import render
from django.template import RequestContext as ctx

from .models import Web


def home(request):
    PAGINACION = 6
    webs = Web.objects.all().order_by('fecha_de_revision')[:PAGINACION]

    return render(request, 'web/home.html', locals())


def websites(request):
    webs = Web.objects.all().order_by('fecha_de_revision')

    return render(request, 'web/websites.html', locals())
