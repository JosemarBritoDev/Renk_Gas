from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Perfil(models.TextChoices):
        ADMIN = "ADMIN", "Gestão / Administrador"
        ENTREGADOR = "ENTREGADOR", "Entregador"
        CLIENTE = "CLIENTE", "Cliente"

    role = models.CharField(
        "Perfil de Acesso",
        max_length=20, 
        choices=Perfil.choices, 
        default=Perfil.CLIENTE
    )
    telefone = models.CharField("Telefone / WhatsApp", max_length=20, blank=True)
    aprovado = models.BooleanField("Aprovado pela Gestão", default=False)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def save(self, *args, **kwargs):
        # Clientes e Administradores são aprovados automaticamente
        if self.role in [self.Perfil.CLIENTE, self.Perfil.ADMIN]:
            self.aprovado = True
        super().save(*args, **kwargs)