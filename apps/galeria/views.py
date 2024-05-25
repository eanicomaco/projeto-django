from django.shortcuts import render, get_object_or_404
from apps.galeria.models import Fotografia

# INDEX TRAZENDO TODOS OS ITENS NA PÁGINA
# def index(request):
#     fotografias = Fotografia.objects.all()
#     return render(request, 'galeria/index.html',{'cards':fotografias})

# INDEX COM FILTRO | Lista apenas objetos ativos
# def index(request):
#     fotografias = Fotografia.objects.filter(ativo=True)
#     return render(request, 'galeria/index.html',{'cards':fotografias})

# INDEX COM FILTRO  E ORDER_BY
def index(request):
    fotografias = Fotografia.objects.order_by('nome').filter(ativo=True)
    return render(request, 'galeria/index.html',{'cards':fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{'fotografia':fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by('nome').filter(ativo=True)

    if "buscar" in request.GET:
        criterio = request.GET['buscar']
        if criterio:
            fotografias = fotografias.filter(nome__icontains=criterio) #icontains é tipo LIKE '%crit%'
    return render(request, "galeria/buscar.html",{'cards':fotografias})
