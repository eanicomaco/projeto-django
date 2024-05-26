from django.urls import path
from apps.galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>/show', imagem, name='imagem.show'),
    path('buscar/', buscar, name='buscar'),
]
