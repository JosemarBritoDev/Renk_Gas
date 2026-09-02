from django.urls import path
from .views import novo_pedido

urlpatterns = [
    path('pedidos/novo/', novo_pedido, name='novo_pedido'),
]