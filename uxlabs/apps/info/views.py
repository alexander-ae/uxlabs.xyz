from django.shortcuts import render

from .models import SeccionNosotros, SeccionLegal


def nosotros(request):
    secciones = SeccionNosotros.objects.all().order_by('position')

    return render(request, 'info/nosotros.html', locals())


def legal(request):
    secciones = SeccionLegal.objects.all().order_by('position')

    return render(request, 'info/legal.html', locals())
