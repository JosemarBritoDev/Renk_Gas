from django.urls import path
from . import views

app_name = "deliveries"

urlpatterns = [
    path("novo/", views.criar_pedido_view, name="criar_pedido"),
    path("meus-pedidos/", views.meus_pedidos_view, name="meus_pedidos"),
    path("painel-entregador/", views.painel_entregador_view, name="painel_entregador"),
    path("pedido/<int:pedido_id>/status/<str:novo_status>/", views.atualizar_status_pedido_view, name="atualizar_status_pedido"),
]