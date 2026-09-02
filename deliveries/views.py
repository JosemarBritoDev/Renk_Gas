from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CriarPedidoForm

@login_required
def novo_pedido(request):
    if request.method == "POST":
        form = CriarPedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.cliente = request.user
            
            # Validação simples de estoque
            if pedido.produto.quantidade_estoque < pedido.quantidade:
                messages.error(request, f"Estoque insuficiente. Restam apenas {pedido.produto.quantidade_estoque} unidades.")
                return render(request, "deliveries/novo_pedido.html", {"form": form})
            
            # Abate do estoque e salva
            pedido.produto.quantidade_estoque -= pedido.quantidade
            pedido.produto.save()
            pedido.save()
            
            messages.success(request, "Pedido realizado com sucesso! Aguarde a entrega.")
            return redirect("dashboard_cliente")
    else:
        form = CriarPedidoForm()

    return render(request, "deliveries/novo_pedido.html", {"form": form})