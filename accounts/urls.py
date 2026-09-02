from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import cadastro_cliente, cadastro_entregador, CustomLoginView, dashboard_cliente, dashboard_entregador

urlpatterns = [
    path('login/', CustomLoginView.as_class() if hasattr(CustomLoginView, 'as_class') else CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastro/', cadastro_cliente, name='cadastro_cliente'),
    path('cadastro/entregador/', cadastro_entregador, name='cadastro_entregador'),
    path('painel/cliente/', dashboard_cliente, name='dashboard_cliente'),
    path('painel/entregador/', dashboard_entregador, name='dashboard_entregador'),
]