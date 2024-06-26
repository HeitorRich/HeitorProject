from django.contrib import admin
from HeitorApp.models import Produto, Categoria, Fornecedor


# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    # colunas exibidas
    list_display = ['id', 'nome_do_produto', 'preco', 'estoque', 'ativo']
    # colunas com link para editar
    list_display_links = ['id', 'nome_do_produto']
    # colunas para filtro
    list_filter = ['preco', 'ativo', 'categoria']
    # buscar por nome
    search_fields = ['nome_do_produto']
    filter_horizontal = ['fornecedor']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_da_categoria']
    list_display_links = ['id', 'nome_da_categoria']
    search_fields = ['nome_da_categoria']


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Fornecedor)