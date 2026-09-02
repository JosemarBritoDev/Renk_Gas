from django.db import models
from django.conf import settings

class Pedido(models.Model):
    class StatusPedido(models.TextChoices):
        PENDENTE = "PENDENTE", "Pendente"
        EM_ROTA = "EM_ROTA", "Em Rota de Entrega"
        ENTREGUE = "ENTREGUE", "Entregue"
        CANCELADO = "CANCELADO", "Cancelado"

    class BairrosAtendidos(models.TextChoices):
        JARDIM_CAMPOS = "Jardim Campos", "Jardim Campos"
        JARDIM_NAZARE = "Jardim Nazaré", "Jardim Nazaré"
        JARDIM_ROBRU = "Jardim Robru", "Jardim Robru"
        VILA_LOURDES = "Vila Lourdes", "Vila Lourdes"

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="pedidos_cliente",
        verbose_name="Cliente"
    )
    entregador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pedidos_entregador",
        verbose_name="Entregador Designado"
    )
    bairro = models.CharField(
        "Bairro de Entrega",
        max_length=50,
        choices=BairrosAtendidos.choices
    )
    endereco = models.CharField("Endereço Completo", max_length=255)
    quantidade_gas = models.PositiveIntegerField("Quantidade de Botijões", default=1)
    status = models.CharField(
        "Status do Pedido",
        max_length=20,
        choices=StatusPedido.choices,
        default=StatusPedido.PENDENTE
    )
    observacao = models.TextField("Observações", blank=True)
    criado_em = models.DateTimeField("Data do Pedido", auto_now_add=True)
    atualizado_em = models.DateTimeField("Última Atualização", auto_now=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-criado_em"]

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.username} ({self.status})"