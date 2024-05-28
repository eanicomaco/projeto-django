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
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem editada com sucesso!')
            return redirect('index')

    return render(request, 'apps/imagens/edit.html', {'form':form, 'foto_id':foto_id})

def imagem_delete(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Imagem excluída com sucesso!')
    return redirect('index')

def imagem_search(request):
    if 'search' in request.GET:
        criterio = request.GET['search']
        fotografias = Fotografia.objects.order_by('nome').filter(ativo=True, nome__icontains=criterio) #icontains é tipo LIKE '%crit%'
    return render(request, "apps/imagens/index.html",{'cards':fotografias})

def imagem_filter(request, filter):
    fotografias = Fotografia.objects.order_by('nome').filter(ativo=True, categoria=filter)
    return render(request, 'apps/imagens/index.html',{'cards':fotografias})
