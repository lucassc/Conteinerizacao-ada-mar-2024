# Exercícios de fixação Aula 2

## Exercícios sobre Dockerfile

### Exercício 1: Criar um Dockerfile Simples

Objetivo: Praticar a criação de um Dockerfile.

    Crie um Dockerfile que use a imagem base alpine e execute o comando echo "Hello, Docker!".

### Exercício 2: Construir uma Imagem a partir de um Dockerfile

Objetivo: Aprender a construir uma imagem Docker usando um Dockerfile.

    Usando o Dockerfile criado no Exercício 1, construa a imagem e nomeie-a hello-docker.

### Exercício 3: Executar um Script com Dockerfile

Objetivo: Executar scripts dentro de containers.

    Modifique o Dockerfile para copiar um script shell local para dentro da imagem e executá-lo quando o container iniciar. O script pode ser simples, como imprimir a data e hora atual.

## Exercícios sobre Docker Volumes

### Exercício 4: Criar e Usar um Docker Volume

Objetivo: Praticar a criação e uso de volumes Docker.

    Crie um volume Docker e inicie um container que use esse volume para armazenar dados. Verifique se os dados persistem após o container ser parado ou removido.

### Exercício 5: Compartilhar Dados entre Containers com Volumes

Objetivo: Aprender a compartilhar dados entre containers usando volumes.

    Crie dois containers que compartilhem o mesmo volume Docker e verifique se podem acessar e modificar os mesmos dados.

## Exercícios sobre Docker Registry/Hub

### Exercício 6: Enviar (push) uma Imagem para o Docker Hub

Objetivo: Praticar o envio de imagens para um repositório remoto.

    Faça login no Docker Hub, marque (tag) a imagem hello-docker criada no Exercício 2 com o seu nome de usuário do Docker Hub e envie-a para o repositório.

### Exercício 7: Baixar (pull) e Rodar uma Imagem do Docker Hub

Objetivo: Aprender a baixar e executar imagens de um repositório remoto.

    Encontre uma imagem interessante no Docker Hub e execute um container usando essa imagem.