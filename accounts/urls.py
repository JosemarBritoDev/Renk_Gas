from django.urls import path
from .views import cadastro_cliente

urlpatterns = [
    path('cadastro/', cadastro_cliente, name='cadastro_cliente'),
]