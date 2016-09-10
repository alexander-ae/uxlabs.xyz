from django.shortcuts import render
from django.template import RequestContext as ctx

from .models import SeccionNosotros


def nosotros(request):
    secciones = SeccionNosotros.objects.all().order_by('position')

    return render(request, 'info/nosotros.html', locals())
