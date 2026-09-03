from django.urls import path
from . import views

app_name = "deliveries"

urlpatterns = [
    path("novo/", views.criar_pedido_view, name="criar_pedido"),
    path("meus-pedidos/", views.meus_pedidos_view, name="meus_pedidos"),
]