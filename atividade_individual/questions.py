import redis
import datetime
import time
import sys
import re
import os

redis_host = os.environ['REDIS_HOST']
redis_password = os.environ['REDIS_PASSWORD']

print("Olá! ...\n")

if not redis_password or not redis_host:
    print("Voce precisa informar as variabens de ambiente 'REDIS_HOST' e 'REDIS_PASSWORD', começe novamente\n")
    time.sleep(1)
    print("Tchau tchau!")
    time.sleep(1)
    sys.exit

# Connect to Redis
redis_conn = redis.Redis(host=redis_host, port=6380, db=0, password=redis_password, ssl=True)
time.sleep(0.3)
print("Validando a sua conexão...")
if not redis_conn.ping():
    print("\nSenha do Redis, REDIS_PASSWORD, não está correta! \n")
    time.sleep(0.3)
    print("Tchau tchau!")
    time.sleep(0.3)
    sys.exit

time.sleep(0.3)
print("Tudo certo, vamos começar!\n")
time.sleep(0.5)
now = datetime.datetime.now()


name = input("Como posso chamar você? ")
time.sleep(0.5)
email = input(f"{name}, qual é o seu email? ")
time.sleep(0.3)

if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Email inválido, começe novamente\n")
    time.sleep(0.5)
    print("Tchau tchau!")
    time.sleep(1)
    redis_conn.close()
    sys.exit(1)
else: 
    print("Seu email é válido, muito obrigado!\n")
    time.sleep(1)
    print("xD\n")
    time.sleep(1)

exist = redis_conn.exists(email)

if exist:
    print("Vefiquei aqui e você já passou por aqui, gostaria de começar novamente?")
    time.sleep(0.5)
    option = input("1 - SIM\n2 - NÃO\n\nSua resposta: ")
    time.sleep(0.2)
    print("")
    time.sleep(0.2)
    if option == "2":
        print("Tchau tchau!")
        redis_conn.close()
        sys.exit(1)
    
    redis_conn.rpush(email, "restart-------------------")

redis_conn.rpush(email, name)
redis_conn.rpush(email, str(now))
    

print("Agora você poderá responder algumas questoes..\n")
time.sleep(0.5)
time.sleep(0.6)

## Question 1
print(f"{name}, é correto afirmar que MAQUINAS VIRTUAIS são mais eficientes que CONTAINERS para rodar aplicacoes?\n")
time.sleep(2)
opcao=input("1 - SIM\n2 - NÃO\n\nSua resposta: ")
redis_conn.rpush(email, f"resposta 1 - {opcao}")
time.sleep(0.1)
print("Resposta computada\n")
time.sleep(0.5)

## Question 2
print("Escreva como a primeira linha do dockerfile, 'FROM ...' deve ser escrito para usar como base a imagem alpine na versão 3 \n")
time.sleep(2)
opcao=input("FROM ")
redis_conn.rpush(email, f"resposta 2 - {opcao}")
time.sleep(0.1)
print("Resposta computada\n")
time.sleep(0.5)

## Question 3
print("Você precisa mover o arquivo 'script.sh' para a pasta '/scripts/'.")
time.sleep(0.5)
print("Complete a linha abaixo:")
time.sleep(2)
opcao=input("COPY ./script.sh ")
redis_conn.rpush(email, f"resposta 3 - {opcao}")
time.sleep(0.1)
print("Resposta computada\n")

time.sleep(2)
print(f"\n\n{name}, finalizamos por aqui. Muito obrigado!\n")
time.sleep(1)
print("Tchau tchau!\n")
redis_conn.close()

