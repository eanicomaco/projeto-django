from django.contrib import admin
from apps.galeria.models import Fotografia

class ListarFotografia(admin.ModelAdmin):
    list_display = ('id','nome','categoria', 'legenda','descricao', 'foto', 'data_fotografia', 'ativo')
    list_display_links = ('id','nome') # informa qual atributo envia para tela de edição
    search_fields = ('nome',) # tem que colocar uma vírgula no final
    list_filter = ('categoria','usuario_id',) # tem que colocar uma vírgula no final
    list_per_page = 10 # cria um paginador
    list_editable = ('ativo',) # permite editar o atributo diretamente no grid
    ordering = ('nome',) #modifica a ordenação do painel admin

admin.site.register(Fotografia,ListarFotografia)
