# Exercícios de fixação Aula 1

## Exercício 1: Rodando seu primeiro container

Objetivo: Aprender a rodar um container Docker utilizando uma imagem pré-existente.

    Use o comando docker run hello-world para rodar um container com a imagem hello-world. Este comando baixa uma imagem simples do Docker Hub e a executa, mostrando uma mensagem no terminal.

## Exercício 2: Listando containers

Objetivo: Aprender a listar containers ativos e inativos.

    Utilize o comando docker ps para listar todos os containers ativos.
    Para ver todos os containers, ativos e inativos, use docker ps -a.

## Exercício 3: Executando um container interativo

Objetivo: Praticar a execução de um container em modo interativo.

    Execute o comando docker run -it ubuntu bash para rodar um container com a imagem do Ubuntu em modo interativo (-it), e você será levado para o bash do container. Explore o container utilizando comandos como ls, cat /etc/os-release, etc.
    Saia do container digitando exit.

## Exercício 4: Parando e removendo containers

Objetivo: Aprender a parar e remover containers.

    Utilize docker ps -a para encontrar o ID ou o nome de um container que você deseja parar.
    Pare o container com docker stop <container_id ou container_name>.
    Remova o container com docker rm <container_id ou container_name>.

## Exercício 5: Trabalhando com imagens Docker

Objetivo: Aprender a buscar, baixar e listar imagens Docker.

    Use docker search ubuntu para buscar por imagens do Ubuntu no Docker Hub.
    Baixe uma imagem do Ubuntu usando docker pull ubuntu.
    Liste todas as imagens disponíveis localmente com docker images.

## Exercício 6: Criando e executando um container com mapeamento de porta

Objetivo: Aprender a criar um container que executa um servidor web simples e mapear a porta do container para uma porta do host.

    Use a imagem nginx para rodar um servidor web: docker run -d -p 8080:80 nginx.
    Acesse o servidor web abrindo http://localhost:8080 no seu navegador. O -d roda o container em modo "detached", e -p mapeia a porta 80 do container para a porta 8080 do seu host.

## Atividade para testar antes da aula 2 

Execute o `build` e `run` do projeto [java-container-example](https://github.com/lucassc/java-container-example?tab=readme-ov-file#build-e-run)

