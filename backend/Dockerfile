FROM python:3.10-slim

WORKDIR /app

# Copia tudo para dentro do container
COPY . .

# Entra na pasta backend
WORKDIR /app/backend

# Instala dependências
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
