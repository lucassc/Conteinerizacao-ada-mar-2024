FROM python:latest

ENV REDIS_HOST=conteinerizacao.redis.cache.windows.net

RUN pip install redis

WORKDIR /app

COPY questions.py /app

CMD ["python", "questions.py"]