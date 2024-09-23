# Projeto de API e Script para Processamento de Dados

Este projeto consiste em uma API simples construída com Flask e um script Python que consome dados dessa API, processa-os e armazena-os em um banco de dados SQLite. A aplicação inclui funcionalidade de agendamento de tarefas recorrentes para automatizar a coleta de dados.
Funcionalidades

    API REST que retorna dados simulados.
    Script que consome dados da API, processa os dados e os armazena em um banco de dados SQLite.
    Uso de variáveis de ambiente para configurações.
    Agendamento para coleta automática de dados a cada hora.

Requisitos

Antes de iniciar, certifique-se de ter instalado os seguintes softwares:

    Python 3.8 ou superior
    Pip (gerenciador de pacotes do Python)
    SQLite (integrado com Python)

Instalação

    Clone o repositório em sua máquina local:

    bash

git clone https://github.com/seu-usuario/nome-do-repositorio.git

Navegue até o diretório do projeto:

bash

cd nome-do-repositorio

Crie um ambiente virtual para o projeto (opcional, mas recomendado):

bash

python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

Instale as dependências do projeto:

bash

pip install -r requirements.txt

Crie um arquivo .env para armazenar as configurações de ambiente. Você pode usar o seguinte template:

bash

touch .env

No arquivo .env, insira as seguintes variáveis:

bash

    API_URL=http://127.0.0.1:5000/data
    DB_PATH=database.db

Configuração e Execução
1. Executar a API

A API é responsável por fornecer os dados simulados. Para rodar a API:

bash

python app.py

A API ficará disponível em http://127.0.0.1:5000.
2. Executar o Script Python

O script coleta dados da API, processa-os e armazena no banco de dados SQLite. Para rodar o script:

bash

python script.py

O script executará a coleta de dados imediatamente e, em seguida, agendará a coleta a cada hora. Certifique-se de que a API esteja rodando antes de executar o script.
3. Verificar o Banco de Dados

Os dados serão armazenados em um arquivo SQLite (database.db). Você pode usar um navegador SQLite para visualizar os dados ou rodar comandos SQL diretamente no terminal.

bash

sqlite3 database.db

Dentro do console SQLite, você pode verificar os dados com:

sql

SELECT * FROM items;

Estrutura do Projeto

plaintext

|-- app.py            # API Flask
|-- script.py         # Script para consumir a API e processar dados
|-- config.py         # Configurações do projeto (API_URL, DB_PATH)
|-- database.py       # Funções para gerenciamento do banco de dados
|-- requirements.txt  # Dependências do projeto
|-- .env              # Variáveis de ambiente (API URL e caminho do banco de dados)
|-- README.md         # Instruções e documentação

Dependências

Todas as dependências do projeto estão listadas no arquivo requirements.txt. As principais bibliotecas são:

    Flask: Para construir a API.
    requests: Para consumir a API no script.
    schedule: Para agendamento de tarefas.
    python-dotenv: Para carregar variáveis de ambiente a partir do arquivo .env.

Instale as dependências com:

bash

pip install -r requirements.txt

Agendamento de Tarefas

O agendamento de tarefas foi implementado com a biblioteca schedule. No código script.py, a função job() é agendada para rodar a cada hora:

python

schedule.every(1).hour.do(job)

Se quiser alterar a frequência do agendamento, você pode modificar essa linha. Por exemplo, para executar a cada 30 minutos, use:

python

schedule.every(30).minutes.do(job)

Contribuições

Contribuições são bem-vindas! Para contribuir, siga estes passos:

    Faça um fork do repositório.
    Crie uma branch para sua feature (git checkout -b feature/nova-feature).
    Faça o commit de suas alterações (git commit -m 'Adiciona nova feature').
    Envie suas mudanças para o repositório remoto (git push origin feature/nova-feature).
    Crie um Pull Request.

Licença

