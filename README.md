# Stripe Integration Flask

Stripe Integration Flask é uma aplicação web simples desenvolvida em Flask que demonstra a integração com o Stripe para lidar com pagamentos. Os usuários podem comprar "O Produto" por R$50.

## Início Rápido

### Pré-requisitos

- Python 3
- Flask
- Conta no Stripe

### Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/your-username/leo-store.git
   cd stripe-integration-flask
   ```
2. **Crie um ambiente virtual e ative:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate caso use Linux, se Windows: venv/Scripts/Activate
    ```
3. **Instale as dependências necessárias:**
   ```bash
   pip install -r requirements.txt
   ```
4. Crie um arquivo .env baseado no .env-example

5. **Execute a aplicação:**
   ```bash
   python run.py
    ```
### Utilizar Docker na aplicação
1. **Certifique-se de ter Docker instalado em sua máquina.**
2. **Execute o comando:**
   ```bash
   docker-compose up --build
   ```
3. Pronto, aplicação inicializada baseada com Docker.

### Estrutura do projeto:
    src/config/config.py: Arquivo de configuração contendo as chaves da API do Stripe.
    src/controllers/stripe_controller.py: Módulo do controlador que lida com as sessões de checkout do Stripe.
    src/routes.py: Rotas da aplicação Flask e lógica principal.
    env-example: Exemplo de arquivo de variáveis de ambiente.
    run.py: Script para executar a aplicação Flask.
    src/templates/index.html: Modelo HTML para a página principal.
    src/templates/thanks.html: Modelo HTML para a página de agradecimento.
    src/templates/failure.html: Modelo HTML para a página de falha no pagamento.
    src/static/script-ajax.js: Arquivo JavaScript para manipular pagamentos do Stripe usando AJAX.
    src/static/script-no-ajax.js: Arquivo JavaScript para manipular pagamentos do Stripe sem AJAX.
