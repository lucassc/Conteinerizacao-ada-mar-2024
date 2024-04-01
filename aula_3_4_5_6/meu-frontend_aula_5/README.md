# Meu frontend aula 5

## Site com index.html personalizado

```BASH
## Primeiro move para a pasta 
cd aula_3_4_5/meu-frontend_aula_5/

## Comando com colume para os logs
docker build -t meu-site .

## Rodar
#      acao  remove  nome-do-container         maquina:conatiner    imagem
docker run   --rm    --name meu-site-container -p 8080:80           meu-site
```


## Volume para os logs

```BASH
## Comando com colume para os logs
docker run -p 8080:80 --rm -d  --name teste-volume --mount type=bind,source=/workspaces/conteinerizacao-ada-mar-2024/aula_3_4_5_6/meu-frontend_aula_5/logs,target=/var/log/nginx/ nginx:latest
```

Agora verifique a [pasta logs](./logs/)
