from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CadastroClienteForm

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