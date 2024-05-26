from django.shortcuts import render, get_object_or_404
from apps.imagens.models import Fotografia

# INDEX TRAZENDO TODOS OS ITENS NA PÁGINA
# def index(request):
#     fotografias = Fotografia.objects.all()
#     return render(request, 'imagens/index.html',{'cards':fotografias})

# INDEX COM FILTRO | Lista apenas objetos ativos
# def index(request):
#     fotografias = Fotografia.objects.filter(ativo=True)
#     return render(request, 'imagens/index.html',{'cards':fotografias})

# INDEX COM FILTRO  E ORDER_BY
def index(request):
    fotografias = Fotografia.objects.order_by('nome').filter(ativo=True)
    return render(request, 'apps/imagens/index.html',{'cards':fotografias})

def imagem_show(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'apps/imagens/show.html',{'fotografia':fotografia})

def imagem_search(request):
    fotografias = Fotografia.objects.order_by('nome').filter(ativo=True)

    if "search" in request.GET:
        criterio = request.GET['search']
        if criterio:
            fotografias = fotografias.filter(nome__icontains=criterio) #icontains é tipo LIKE '%crit%'
    return render(request, "apps/imagens/search.html",{'cards':fotografias})

def imagem_create(request):
    return render(request, 'apps/imagens/create.html')

def imagem_edit(request, foto_id):
    pass

def imagem_delete(request, foto_id):
    pass
