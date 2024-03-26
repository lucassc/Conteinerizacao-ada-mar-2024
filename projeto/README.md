# Projeto: Conteinerização do "Sistema de Casa de Eventos" para Implantação Global

## Contexto do Problema

Você desenvolveu um inovador "Sistema de Casa de Eventos", que facilita a gestão de reservas, eventos e vendas de ingressos. Esta aplicação se tornou extremamente popular em sua região e agora atraiu a atenção de uma grande empresa internacional de eventos. Eles desejam implementar sua solução em várias localidades ao redor do mundo. No entanto, enfrentam um desafio significativo: garantir que o sistema possa ser facilmente implantado, escalado e mantido em diferentes ambientes de computação.

## Seu Desafio

Sua tarefa é conteinerizar o [Sistema de Casa de Eventos](https://github.com/roofranklin/casa-de-eventos-react), criando um Dockerfile robusto que permita que qualquer equipe, em qualquer parte do mundo, possa implantar e executar sua aplicação com facilidade, independentemente da configuração do ambiente local deles.

## Objetivos

- **Conteinerização:** Prepare seu "Sistema de Casa de Eventos" para implantação global usando Docker.
- **Simplicidade:** Assegure que o processo de implantação seja simples, exigindo comandos mínimos para iniciar a aplicação.
- **Documentação:** Forneça documentação clara para que equipes de diferentes níveis técnicos possam compreender e executar o processo.

## Requisitos

- Acesso à Internet e um computador capaz de executar Docker.
- Conhecimento básico de Docker, incluindo construção de imagens e contêineres.
- Uma conta no [Docker Hub](https://hub.docker.com/) para publicar a imagem.

## Instruções Detalhadas

### Parte 1: Preparando o Dockerfile

1. **Criação do Dockerfile:** Na raiz do seu projeto "Sistema de Casa de Eventos", crie um Dockerfile detalhado. Este deve especificar a imagem base, dependências, variáveis de ambiente, portas e o comando para iniciar a aplicação. Voce pode copiar o repositório ou criar um [fork](https://github.com/roofranklin/casa-de-eventos-react/fork).

### Parte 2: Construção e Testes Locais

2. **Build da Imagem:** Utilize o `docker build` para criar a imagem Docker baseada em seu Dockerfile.
3. **Testes:** Execute sua imagem localmente para assegurar que o sistema funciona corretamente dentro do contêiner.

### Parte 3: Publicação no Docker Hub

4. **Tagging e Publicação:** Após a verificação local, marque sua imagem com seu username do Docker Hub e a versão da aplicação, e então publique-a usando `docker push`.

## Critérios de Avaliação

- **Funcionalidade:** A aplicação deve funcionar sem falhas dentro do contêiner.
- **Dockerfile:** O Dockerfile deve ser bem organizado e otimizado para eficiência.
- **Documentação:** Inclua um README.md explicando como construir, executar e usar sua imagem Docker.

## Entrega

- **Formato:** Envie o link para o repositório GitHub contendo o código fonte e o Dockerfile, além do link para a imagem no Docker Hub.

Este projeto é uma oportunidade para demonstrar suas habilidades em conteinerização e preparação de aplicativos para implantação global. Boa sorte!
