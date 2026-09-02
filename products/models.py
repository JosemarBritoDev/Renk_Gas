from django.db import models

class Produto(models.Model):
    nome = models.CharField("Nome do Produto", max_length=100)
    descricao = models.TextField("Descrição", blank=True)
    preco = models.DecimalField("Preço de Venda (R$)", max_digits=8, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField("Quantidade em Estoque", default=0)
    ativo = models.BooleanField("Ativo para Venda", default=True)
    criado_em = models.DateTimeField("Cadastrado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("Última Atualização", auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - R$ {self.preco} (Estoque: {self.quantidade_estoque})"
