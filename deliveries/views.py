from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pedido, Bairro
from products.models import Produto

@login_required
def criar_pedido_view(request):
    bairros = Bairro.objects.filter(ativo=True)
    produtos = Produto.objects.filter(ativo=True)

    if request.method == "POST":
        produto_id = request.POST.get("produto")
        bairro_id = request.POST.get("bairro")
        quantidade = int(request.POST.get("quantidade", 1))
        endereco = request.POST.get("endereco_entrega")
        forma_pagamento = request.POST.get("forma_pagamento")
        observacoes = request.POST.get("observacoes", "")

        produto = get_object_or_404(Produto, id=produto_id)
        bairro = get_object_or_404(Bairro, id=bairro_id)

        if produto.quantidade_estoque < quantidade:
            messages.error(request, f"Estoque insuficiente. Restam {produto.quantidade_estoque} unidades.")
            return render(request, "deliveries/criar_pedido.html", {
                "bairros": bairros,
                "produtos": produtos
            })

        # Abate do estoque
        produto.quantidade_estoque -= quantidade
        produto.save()

        # Criação do pedido
        Pedido.objects.create(
            cliente=request.user,
            produto=produto,
            quantidade=quantidade,
            bairro=bairro,
            endereco_entrega=endereco,
            forma_pagamento=forma_pagamento,
            observacoes=observacoes
        )

        messages.success(request, "Pedido realizado com sucesso!")
        return redirect("deliveries:meus_pedidos")

    return render(request, "deliveries/criar_pedido.html", {
        "bairros": bairros,
        "produtos": produtos
    })


@login_required
def meus_pedidos_view(request):
    """Exibe o histórico de pedidos do cliente logado."""
    pedidos = Pedido.objects.filter(cliente=request.user).select_related('produto', 'bairro').order_by('-criado_em')
    return render(request, "deliveries/meus_pedidos.html", {"pedidos": pedidos})

@login_required
def painel_entregador_view(request):
    """Exibe o painel de entregas pendentes e em rota para o entregador."""
    pedidos_pendentes = Pedido.objects.filter(status='PENDENTE').select_related('cliente', 'produto', 'bairro').order_by('criado_em')
    meus_pedidos_em_rota = Pedido.objects.filter(entregador=request.user, status='EM_ROTA').select_related('cliente', 'produto', 'bairro').order_by('criado_em')

    return render(request, "deliveries/painel_entregador.html", {
        "pedidos_pendentes": pedidos_pendentes,
        "meus_pedidos_em_rota": meus_pedidos_em_rota,
    })

@login_required
def atualizar_status_pedido_view(request, pedido_id, novo_status):
    """Atualiza o status do pedido (muda para EM_ROTA ou ENTREGUE)."""
    pedido = get_object_or_404(Pedido, id=pedido_id)

    if novo_status == 'EM_ROTA' and pedido.status == 'PENDENTE':
        pedido.status = 'EM_ROTA'
        pedido.entregador = request.user
        pedido.save()
        messages.success(request, f"Você assumiu a entrega do Pedido #{pedido.id}!")
    elif novo_status == 'ENTREGUE' and pedido.status == 'EM_ROTA':
        pedido.status = 'ENTREGUE'
        pedido.save()
        messages.success(request, f"Pedido #{pedido.id} marcado como ENTREGUE!")
    else:
        messages.error(request, "Ação de alteração de status inválida.")

    return redirect("deliveries:painel_entregador")