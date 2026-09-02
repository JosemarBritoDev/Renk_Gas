from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Pedido

@admin.register(Pedido)
class PedidoAdmin(ModelAdmin):
    list_display = ("id", "cliente", "bairro", "quantidade_gas", "status", "entregador", "criado_em")
    list_filter = ("status", "bairro", "criado_em")
    search_fields = ("cliente__username", "endereco", "bairro")
    list_editable = ("status", "entregador")