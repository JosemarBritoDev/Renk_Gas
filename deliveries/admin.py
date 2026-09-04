from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Bairro, Pedido


@admin.register(Bairro)
class BairroAdmin(ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)


@admin.register(Pedido)
class PedidoAdmin(ModelAdmin):
    list_display = ('id', 'cliente', 'produto', 'quantidade', 'status', 'criado_em')
    list_filter = ('status', 'bairro', 'criado_em')
    search_fields = ('cliente__username', 'endereco_entrega')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            # Trava todos os campos se já foi entregue
            if obj.status == 'entregue':
                return [f.name for f in self.model._meta.fields]
            # Caso contrário, libera apenas a troca de status
            return [f.name for f in self.model._meta.fields if f.name != 'status']
        return super().get_readonly_fields(request, obj)

    def has_change_permission(self, request, obj=None):
        # Desativa o botão de salvar/editar no painel para pedidos já entregues
        if obj and obj.status == 'entregue':
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.status == 'entregue':
            return False
        return super().has_delete_permission(request, obj)