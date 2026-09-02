from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.forms import CadastroClienteForm, CadastroEntregadorForm
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

        

class TesteFormulariosCadastro(TestCase):

    def test_form_cadastro_cliente_valido(self):
        dados = {
            "username": "clienteform",
            "first_name": "Cliente Teste",
            "email": "cliente@email.com",
            "telefone": "11988887777",
            "password1": "SenhaForte123!",
            "password2": "SenhaForte123!"
        }
        form = CadastroClienteForm(data=dados)
        self.assertTrue(form.is_valid())
        usuario = form.save()
        self.assertEqual(usuario.role, User.Perfil.CLIENTE)
        self.assertTrue(usuario.aprovado)

    def test_form_cadastro_entregador_pendente(self):
        dados = {
            "username": "entregadorform",
            "first_name": "Entregador Teste",
            "email": "entregador@email.com",
            "telefone": "11977776666",
            "password1": "SenhaForte123!",
            "password2": "SenhaForte123!"
        }
        form = CadastroEntregadorForm(data=dados)
        self.assertTrue(form.is_valid())
        usuario = form.save()
        self.assertEqual(usuario.role, User.Perfil.ENTREGADOR)
        self.assertFalse(usuario.aprovado)