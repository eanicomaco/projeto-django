from django.shortcuts import redirect, render, get_object_or_404
from apps.imagens.models import Fotografia
from apps.imagens.forms import FotografiaForms
from django.contrib import messages


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
    if not request.user.is_authenticated:
        messages.error(request,'Você precisa estar logado para acessar essa funcionalidade.')
        return redirect('login')

    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Imagem cadastrada com sucesso!')
            return redirect('index')
        else:
            messages.error(request, form.errors)
            return redirect('imagem.create')

    return render(request, 'apps/imagens/create.html',{'form':form})

def imagem_edit(request, foto_id):
    pass

def imagem_delete(request, foto_id):
    pass
