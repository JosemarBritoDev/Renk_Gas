from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(ModelAdmin):
    list_display = ("nome", "preco", "quantidade_estoque", "ativo", "atualizado_em")
    list_editable = ("preco", "quantidade_estoque", "ativo")
    search_fields = ("nome", "descricao")
    list_filter = ("ativo",)
