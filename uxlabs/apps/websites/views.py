from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from pure_pagination import Paginator

from .models import Web, Categoria


def home(request):
    PAGINACION = 6
    destacado = Web.objects.all().order_by('fecha_de_revision').first()
    webs = Web.objects.all().order_by('fecha_de_revision')[:PAGINACION]

    return render(request, 'web/home.html', locals())


def websites(request):
    """
        Retorna la lista de websites
    """
    WEBS_POR_PAGINA = 12
    webs = Web.objects.all()

    # parámetros GET
    q_categoria = request.GET.get('categoria', '').strip()
    q = request.GET.get('q', '')

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    categorias = Categoria.objects.all()

    if q_categoria:
        try:
            categoria = Categoria.objects.get(nombre=q_categoria)
        except:
            categoria = None

        if categoria:
            webs = webs.filter(categoria=categoria)

    # búsqueda
    if q and len(q) > 2:
        q1 = Q(nombre__icontains=q)
        q2 = Q(detalle__icontains=q)
        webs = webs.filter(q1 | q2 )

    webs = webs.order_by('fecha_de_revision')

    # paginacion
    p = Paginator(webs, WEBS_POR_PAGINA, request=request)
    lista_webs = p.page(page)


    return render(request, 'web/websites.html', locals())


def detalle(request, slug):
    """
        Retorna el detalle de un website
    """
    web = get_object_or_404(Web, slug=slug)

    return render(request, 'web/detalle.html', locals())
