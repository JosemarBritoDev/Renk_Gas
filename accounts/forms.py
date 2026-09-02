from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class CadastroClienteForm(UserCreationForm):
    telefone = forms.CharField(
        label="Telefone / WhatsApp",
        max_length=20,
        widget=forms.TextInput(attrs={"placeholder": "(11) 99999-9999"})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "email", "telefone")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Perfil.CLIENTE
        user.aprovado = True
        if commit:
            user.save()
        return user


class CadastroEntregadorForm(UserCreationForm):
    telefone = forms.CharField(
        label="Telefone / WhatsApp",
        max_length=20,
        widget=forms.TextInput(attrs={"placeholder": "(11) 99999-9999"})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "email", "telefone")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Perfil.ENTREGADOR
        user.aprovado = False  # Requer aprovação manual do Renato
        if commit:
            user.save()
        return user