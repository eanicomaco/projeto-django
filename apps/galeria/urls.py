from django.urls import path
from apps.galeria.views import index, imagem, buscar
# from galeria.views import imagem --> pode ser feito de forma simplificada, conf. acima

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
]
