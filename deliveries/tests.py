from django.test import TestCase
from django.contrib.auth import get_user_model
from deliveries.models import Pedido

User = get_user_model()

class TesteModeloPedido(TestCase):

    def setUp(self):
        self.cliente = User.objects.create_user(
            username="cliente_renk",
            password="senha_segura_123",
            role=User.Perfil.CLIENTE,
            telefone="11988887777"
        )

    def test_criar_pedido_bairro_valido(self):
        """ Testa a criação de um pedido para a região do Jardim Campos """
        pedido = Pedido.objects.create(
            cliente=self.cliente,
            bairro=Pedido.BairrosAtendidos.JARDIM_CAMPOS,
            endereco="Rua Exemplo, 123",
            quantidade_gas=2
        )
        self.assertEqual(pedido.status, Pedido.StatusPedido.PENDENTE)
        self.assertEqual(pedido.bairro, "Jardim Campos")
        self.assertEqual(pedido.quantidade_gas, 2)