from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import CadastroClienteForm, CadastroEntregadorForm

def cadastro_cliente(request):
    if request.method == "POST":
        form = CadastroClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso! Faça seu login.")
            return redirect("login")
    else:
        form = CadastroClienteForm()
    
    return render(request, "accounts/cadastro_cliente.html", {"form": form})


def cadastro_entregador(request):
    if request.method == "POST":
        form = CadastroEntregadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Cadastro realizado! Sua conta aguarda aprovação da gestão para acesso.")
            return redirect("login")
    else:
        form = CadastroEntregadorForm()
    
    return render(request, "accounts/cadastro_entregador.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        user = self.request.user
        if user.is_staff or user.role == "ADMINISTRADOR":
            return "/admin/"
        elif user.role == "ENTREGADOR":
            return "/painel/entregador/"
        return "/painel/cliente/"


@login_required
def dashboard_cliente(request):
    return render(request, "accounts/dashboard_cliente.html")


@login_required
def dashboard_entregador(request):
    if not request.user.aprovado:
        messages.warning(request, "Sua conta de entregador ainda aguarda aprovação da gestão.")
        return redirect("login")
    return render(request, "accounts/dashboard_entregador.html")