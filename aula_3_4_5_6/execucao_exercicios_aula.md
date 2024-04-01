# Execução exercícios de fixação Aula

## Exercícios sobre Dockerfile

### Exercício 1: Criar um Dockerfile Simples


### Exercício 2: Construir uma Imagem a partir de um Dockerfile


### Exercício 3: Executar um Script com Dockerfile


## Exercícios sobre Docker Volumes

### Exercício 4: Criar e Usar um Docker Volume


### Exercício 5: Compartilhar Dados entre Containers com Volumes

```BASH
## Criar volume
docker volume create exercicio-5

#inicializa container
docker run --name inicializador --rm --mount type=volume,source=exercicio-5,target=/meu-site busybox sh -c 'echo "<h1>Meu site dentro de um docker volume</h1>" > /meu-site/index.html'

docker run --name meu-site --rm -p 8080:80 --mount type=volume,source=exercicio-5,target=/usr/share/nginx/html nginx
```

## Exercícios sobre Docker Registry/Hub

### Exercício 6: Enviar (push) uma Imagem para o Docker Hub


### Exercício 7: Baixar (pull) e Rodar uma Imagem do Docker Hub

