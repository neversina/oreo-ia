FROM python:3.10-slim

WORKDIR /app

# Copia tudo para dentro do container
COPY . .

# Navega para backend
WORKDIR /app/backend

# Instala dependências
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE $PORT

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
