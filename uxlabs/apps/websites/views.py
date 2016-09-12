from django.shortcuts import render
from django.template import RequestContext as ctx

from .models import Web, Categoria


def home(request):
    PAGINACION = 6
    webs = Web.objects.all().order_by('fecha_de_revision')[:PAGINACION]

    return render(request, 'web/home.html', locals())


def websites(request):
    """
        Retorna la lista de websites
    """
    webs = Web.objects.all()

    q_categoria = request.GET.get('categoria', '').strip()

    categorias = Categoria.objects.all()

    if q_categoria:
        try:
            categoria = Categoria.objects.get(nombre=q_categoria)
        except:
            categoria = None

        if categoria:
            webs = webs.filter(categoria=categoria)

    webs = webs.order_by('fecha_de_revision')

    return render(request, 'web/websites.html', locals())
