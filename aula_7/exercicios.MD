# Exercícios de fixação

## Exercício 1: Criar um Arquivo Docker Compose Simples para um Aplicativo Web

**Objetivo:** Praticar a criação de um arquivo `docker-compose.yml` para rodar um aplicativo web simples.

- **Tarefa:**
  - Crie um arquivo `docker-compose.yml` que defina um serviço para rodar um servidor web nginx.
  - Configure o serviço para expor a porta `80` para que o servidor web seja acessível no navegador.
  - Use a imagem oficial `nginx` do Docker Hub.

## Exercício 2: Usar Docker Compose para Orquestrar um Aplicativo Web e um Banco de Dados

**Objetivo:** Aprender a orquestrar múltiplos serviços com Docker Compose, incluindo um aplicativo web e um banco de dados.

- **Tarefa:**
  - Expanda o `docker-compose.yml` do Exercício 1 para incluir um serviço de banco de dados usando a imagem `postgres`.
  - Configure o serviço do banco de dados para usar um volume Docker para persistência de dados.
  - Certifique-se de que o aplicativo web possa se conectar ao banco de dados. (Nota: Você pode usar variáveis de ambiente para configurar a conexão do banco de dados.)

## Exercício 3: Configurar Docker Compose para Usar Variáveis de Ambiente e Networks Personalizadas

**Objetivo:** Praticar o uso de variáveis de ambiente e redes personalizadas no Docker Compose para melhorar a segurança e a comunicação entre serviços.

- **Tarefa:**
  - Modifique o arquivo `docker-compose.yml` criado no Exercício 2.
  - Adicione uma rede personalizada para permitir a comunicação entre o aplicativo web e o serviço de banco de dados.
  - Use um arquivo `.env` para definir variáveis de ambiente, como a senha do banco de dados, e referencie essas variáveis no seu `docker-compose.yml`.
  - Garanta que apenas os serviços necessários possam se comunicar entre si pela rede personalizada.
