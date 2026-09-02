from django import forms
from .models import Pedido, Bairro
from products.models import Produto

CLASSES_INPUT = "w-full bg-gray-700 border border-gray-600 text-white rounded px-3 py-2 focus:outline-none focus:border-purple-500"

class CriarPedidoForm(forms.ModelForm):
    produto = forms.ModelChoiceField(
        queryset=Produto.objects.filter(ativo=True),
        label="Selecione o Produto",
        empty_label="Escolha um produto...",
        widget=forms.Select(attrs={"class": CLASSES_INPUT})
    )
    
    bairro = forms.ModelChoiceField(
        queryset=Bairro.objects.filter(ativo=True),
        label="Bairro para Entrega",
        empty_label="Selecione o bairro...",
        widget=forms.Select(attrs={"class": CLASSES_INPUT})
    )

    class Meta:
        model = Pedido
        fields = ("produto", "quantidade", "bairro", "endereco_entrega", "forma_pagamento", "observacoes")
        widgets = {
            "quantidade": forms.NumberInput(attrs={"class": CLASSES_INPUT, "min": 1, "value": 1}),
            "endereco_entrega": forms.TextInput(attrs={"class": CLASSES_INPUT, "placeholder": "Rua, Número, Complemento"}),
            "forma_pagamento": forms.Select(attrs={"class": CLASSES_INPUT}),
            "observacoes": forms.Textarea(attrs={"class": CLASSES_INPUT, "rows": 3, "placeholder": "Troco para quanto? Ponto de referência..."}),
        }