from django.shortcuts import render
from .models import Cliente, Habitacion, Ocupacion

# Create your views here.
def cliente_detail(request, pk):
    """
    Esta clase implementa la vista de la pagina
    book_detail.html donde se muestra la página de
    detalles de un libro determinado
    AUTOR: Carolina Monedero
    """
    client = Cliente.objects.get(id=pk)
    ocupaciones = []

    for ocs in list(Ocupacion.objects.filter(cliente=client)):
        ocupaciones.append(ocs)

    return render(request, 'cliente_detail.html', context={'ocupaciones': ocupaciones}) # noqa
