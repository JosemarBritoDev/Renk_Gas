from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.admin import ModelAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Campos que aparecem na listagem do painel
    list_display = ("username", "first_name", "role", "telefone", "aprovado", "is_staff")
    
    # Filtros na lateral direita
    list_filter = ("role", "aprovado", "is_staff", "is_active")
    
    # Campos pesquisáveis
    search_fields = ("username", "first_name", "last_name", "email", "telefone")
    
    # Ações em massa no painel (Aprovar Entregadores com 1 clique)
    actions = ["aprovar_usuarios"]

    # Adiciona nossos campos customizados no formulário de edição do usuário
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Informações da Renk Gás", {"fields": ("role", "telefone", "aprovado")}),
    )

    @admin.action(description="Aprovar usuários/entregadores selecionados")
    def aprovar_usuarios(self, request, queryset):
        queryset.update(aprovado=True)
        self.message_user(request, "Usuários selecionados foram aprovados com sucesso!")