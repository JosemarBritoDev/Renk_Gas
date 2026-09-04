from django.db import models, transaction
from django.conf import settings
from django.core.exceptions import ValidationError
from products.models import Produto


class Bairro(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('em_rota', 'Em Rota'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    )

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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def save(self, *args, **kwargs):
        if self.pk:
            pedido_antigo = Pedido.objects.get(pk=self.pk)

            # Baixa no estoque ao mudar status para 'entregue'
            if pedido_antigo.status != 'entregue' and self.status == 'entregue':
                if self.produto.quantidade_estoque < self.quantidade:
                    raise ValidationError(
                        f"Estoque insuficiente para {self.produto.nome}. "
                        f"Disponível: {self.produto.quantidade_estoque}, Solicitado: {self.quantidade}"
                    )
                with transaction.atomic():
                    self.produto.quantidade_estoque -= self.quantidade
                    self.produto.save()

            # Estorno de estoque se sair do status 'entregue' para outro
            elif pedido_antigo.status == 'entregue' and self.status != 'entregue':
                with transaction.atomic():
                    self.produto.quantidade_estoque += self.quantidade
                    self.produto.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.username} ({self.get_status_display()})"