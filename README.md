## 🚚 Renk Gás - Sistema de Gestão de Pedidos e Entregas

Sistema web para gestão de pedidos, controle de estoque e acompanhamento de entregas de gás e água para a empresa **Renk Gás**. O sistema atende especificamente os bairros: **Jardim Campos, Jardim Nazaré, Jardim Robru e Vila Lourdes**.

Desenvolvido por **Brito's Code Tecnologia** | Contacto: (11) 97264-6617

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.14
* **Framework Backend:** Django 6.1
* **Painel Administrativo:** Django Unfold (Tema Escuro Customizado)
* **Estilização Frontend:** Tailwind CSS
* **Banco de Dados:** SQLite (Desenvolvimento)
* **Práticas de Desenvolvimento:** TDD (Test Driven Development)
* **Integração Contínua (CI):** GitHub Actions

---

## 📌 Funcionalidades Implementadas

* **Autenticação Multi-Perfil Customizada:**
  * **Administrador (Gestão):** Acesso total ao painel administrativo.
  * **Cliente:** Cadastro autônomo e liberado instantaneamente.
  * **Entregador:** Cadastro com fluxo de aprovação pendente (requer autorização manual da gestão).
* **Interface e Painel de Controle:**
  * Painel Admin moderno com Django Unfold estilizado em modo escuro e totalmente traduzido para Português (`pt-br`).
  * Páginas de Cadastro (Cliente/Entregador) e Tela de Login responsivas construídas com Tailwind CSS.
  * Redirecionamento dinâmico pós-login de acordo com o perfil do usuário.
* **Módulo de Logística e Pedidos (`deliveries`):**
  * Estrutura de pedidos vinculando cliente, entregador e status do pedido (*Pendente*, *Em Rota*, *Entregue*, *Cancelado*).
  * Validação das regiões de atendimento cobertas pela empresa.
* **Módulo de Produtos e Estoque (`products`):**
  * Cadastro de produtos com nome, descrição, preço de venda e saldo em estoque.
  * Edição rápida de estoque e valores diretamente via painel administrativo.
* **Qualidade e Automação:**
  * Suíte de testes automatizados cobrindo modelos, formulários e rotas de visualização (TDD).
  * Pipeline de CI no GitHub Actions configurada para validação automática de código a cada *push*.

---

## 🛠️ Como Executar o Projeto Localmente

### Pré-requisitos
* Python 3.14+ instalado
* Git instalado

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/Renk_Gas.git](https://github.com/seu-usuario/Renk_Gas.git)
   cd Renk_Gas
