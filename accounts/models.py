from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Perfil(models.TextChoices):
        CLIENTE = 'cliente', 'Cliente'
        ENTREGADOR = 'entregador', 'Entregador'
        ADMIN = 'admin', 'Administrador'

    role = models.CharField(
        max_length=20,
        choices=Perfil.choices,
        default=Perfil.CLIENTE,
        verbose_name="Perfil do Usuário"
    )
    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Telefone / WhatsApp"
    )
    aprovado = models.BooleanField(
        default=True,
        verbose_name="Cadastro Aprovado",
        help_text="Indica se o entregador/usuário foi aprovado para utilizar o sistema."
    )

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        nome = self.get_full_name() or self.username
        return f"{nome} ({self.get_role_display()})"