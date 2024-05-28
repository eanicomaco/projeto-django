from django.urls import path
from apps.imagens.views import \
    index, imagem_show, imagem_create, imagem_edit, imagem_delete, imagem_search, imagem_filter
    #barra invertida permite quebrar linha (pelo visto)

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>/show', imagem_show, name='imagem.show'),
    path('imagem/create', imagem_create, name='imagem.create'),
    path('imagem/<int:foto_id>/edit', imagem_edit, name='imagem.edit'),
    path('imagem/<int:foto_id>/delete', imagem_delete, name='imagem.delete'),
    path('imagem/search', imagem_search, name='imagem.search'),
    path('imagem/<str:filter>/filter', imagem_filter, name='imagem.filter'),
]
