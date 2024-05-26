from django.urls import path
from apps.imagens.views import \
    index, imagem_show, imagem_search, imagem_create, imagem_edit, imagem_delete
    #barra invertida permite quebrar linha (pelo visto)

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>/show', imagem_show, name='imagem.show'),
    path('imagem/search', imagem_search, name='imagem.search'),
    path('imagem/create', imagem_create, name='imagem.create'),
    path('imagem/<int:foto_id>/edit', imagem_edit, name='imagem.edit'),
    path('imagem/<int:foto_id>/delete', imagem_delete, name='imagem.delete'),
]
