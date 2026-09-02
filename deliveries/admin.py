from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Bairro, Pedido

@admin.register(Bairro)
class BairroAdmin(ModelAdmin):
    list_display = ("nome", "ativo")
    list_editable = ("ativo",)
    search_fields = ("nome",)

@admin.register(Pedido)
class PedidoAdmin(ModelAdmin):
    list_display = ("id", "cliente", "produto", "quantidade", "bairro", "status", "criado_em")
    list_filter = ("status", "bairro", "forma_pagamento")