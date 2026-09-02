from django.db import models
from django.conf import settings

class Bairro(models.Model):
    nome = models.CharField("Nome do Bairro", max_length=100, unique=True)
    ativo = models.BooleanField("Ativo para Entregas", default=True)

    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    FORMAS_PAGAMENTO = [
        ("PIX", "PIX"),
        ("CARTAO_DEBITO", "Cartão de Débito"),
        ("CARTAO_CREDITO", "Cartão de Crédito"),
        ("DINHEIRO", "Dinheiro"),
    ]

    STATUS_CHOICES = [
        ("PENDENTE", "Pendente"),
        ("EM_ROTA", "Em Rota"),
        ("ENTREGUE", "Entregue"),
        ("CANCELADO", "Cancelado"),
    ]

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="pedidos"
    )
    entregador = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="entregas"
    )
    produto = models.ForeignKey(
        'products.Produto', 
        on_delete=models.PROTECT
    )
    quantidade = models.PositiveIntegerField(default=1)
    bairro = models.ForeignKey(
        Bairro, 
        on_delete=models.PROTECT, 
        verbose_name="Bairro de Entrega"
    )
    endereco_entrega = models.CharField("Endereço de Entrega", max_length=255)
    forma_pagamento = models.CharField("Forma de Pagamento", max_length=20, choices=FORMAS_PAGAMENTO)
    observacoes = models.TextField("Observações", blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDENTE")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.username} ({self.bairro.nome})"