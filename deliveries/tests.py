from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Pedido, Bairro
from products.models import Produto

User = get_user_model()

class TesteModeloPedido(TestCase):
    def setUp(self):
        self.cliente = User.objects.create_user(
            username="cliente_teste",
            password="SenhaSegura123!"
        )
        self.bairro = Bairro.objects.create(nome="Jardim Campos", ativo=True)
        self.produto = Produto.objects.create(
            nome="Botijão P13",
            preco=110.00,
            quantidade_estoque=10,
            ativo=True
        )

    def test_criar_pedido_bairro_valido(self):
        """Testa a criação de um pedido vinculado a um Bairro e Produto válidos."""
        pedido = Pedido.objects.create(
            cliente=self.cliente,
            produto=self.produto,
            bairro=self.bairro,
            quantidade=1,
            endereco_entrega="Rua das Flores, 123",
            forma_pagamento="PIX"
        )
        self.assertEqual(pedido.bairro.nome, "Jardim Campos")
        self.assertEqual(pedido.produto.nome, "Botijão P13")
        self.assertEqual(pedido.status, "PENDENTE")