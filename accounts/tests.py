from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class TesteModeloUsuario(TestCase):

    def test_criar_usuario_cliente(self):
        """ Testa se o cliente é criado e aprovado automaticamente """
        cliente = User.objects.create_user(
            username="cliente_teste",
            password="senha_segura_123",
            role=User.Perfil.CLIENTE,
            telefone="11988887777"
        )
        self.assertEqual(cliente.role, User.Perfil.CLIENTE)
        self.assertTrue(cliente.aprovado)  # Clientes já nascem aprovados

    def test_criar_usuario_entregador_requer_aprovacao(self):
        """ Testa se o entregador nasce pendente de aprovação pela gestão """
        entregador = User.objects.create_user(
            username="entregador_teste",
            password="senha_segura_123",
            role=User.Perfil.ENTREGADOR,
            telefone="11977776666"
        )
        self.assertEqual(entregador.role, User.Perfil.ENTREGADOR)
        self.assertFalse(entregador.aprovado)  # Entregador depende da aprovação do Renato