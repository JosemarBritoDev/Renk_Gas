from django.db import models
from django.conf import settings
from products.models import Produto

class Bairro(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('EM_ROTA', 'Em Rota'),
        ('ENTREGUE', 'Entregue'),
        ('CANCELADO', 'Cancelado'),
    ]

    PAGAMENTO_CHOICES = [
        ('PIX', 'PIX'),
        ('CARTAO', 'Cartão na Entrega'),
        ('DINHEIRO', 'Dinheiro'),
    ]

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='pedidos_cliente'
    )
    entregador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pedidos_entregador'
    )
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(default=1)
    endereco_entrega = models.CharField(max_length=255)
    forma_pagamento = models.CharField(max_length=20, choices=PAGAMENTO_CHOICES)
    observacoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.username} ({self.status})"