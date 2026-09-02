from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

# Classe base para aplicar o visual escuro do Tailwind em todos os inputs
CLASSES_INPUT = "w-full bg-gray-700 border border-gray-600 text-white rounded px-3 py-2 focus:outline-none focus:border-purple-500"

class CadastroClienteForm(UserCreationForm):
    telefone = forms.CharField(
        label="Telefone / WhatsApp",
        max_length=20,
        widget=forms.TextInput(attrs={"placeholder": "(11) 99999-9999", "class": CLASSES_INPUT})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "email", "telefone")
        widgets = {
            "username": forms.TextInput(attrs={"class": CLASSES_INPUT, "placeholder": "Digite seu usuário"}),
            "first_name": forms.TextInput(attrs={"class": CLASSES_INPUT, "placeholder": "Seu nome completo"}),
            "email": forms.EmailInput(attrs={"class": CLASSES_INPUT, "placeholder": "seu@email.com"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica o estilo do Tailwind nos campos de senha
        if "password1" in self.fields:
            self.fields["password1"].widget.attrs["class"] = CLASSES_INPUT
        if "password2" in self.fields:
            self.fields["password2"].widget.attrs["class"] = CLASSES_INPUT

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
        widget=forms.TextInput(attrs={"placeholder": "(11) 99999-9999", "class": CLASSES_INPUT})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "email", "telefone")
        widgets = {
            "username": forms.TextInput(attrs={"class": CLASSES_INPUT, "placeholder": "Digite seu usuário"}),
            "first_name": forms.TextInput(attrs={"class": CLASSES_INPUT, "placeholder": "Seu nome completo"}),
            "email": forms.EmailInput(attrs={"class": CLASSES_INPUT, "placeholder": "seu@email.com"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "password1" in self.fields:
            self.fields["password1"].widget.attrs["class"] = CLASSES_INPUT
        if "password2" in self.fields:
            self.fields["password2"].widget.attrs["class"] = CLASSES_INPUT

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Perfil.ENTREGADOR
        user.aprovado = False  # Depende da aprovação do Renato
        if commit:
            user.save()
        return user