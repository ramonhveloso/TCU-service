# Etapa 1: Builder
FROM python:3.11.5-slim AS builder

WORKDIR /app

# Instala pacotes de sistema necessários para Poetry e outras dependências
RUN apt-get update && apt-get install -y build-essential libpq-dev curl

# Instala o Poetry
RUN pip install poetry

# Copia apenas os arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock /app/

# Instala as dependências sem criar o ambiente virtual
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-dev --no-interaction --no-ansi

# Etapa 2: Imagem final
FROM python:3.11.5-slim

WORKDIR /app

# Copia o projeto e as dependências da primeira etapa
COPY --from=builder /app /app

# Define a variável de ambiente para o Python do venv
ENV PATH="/app/.venv/bin:$PATH"

# Copia o código restante
COPY . /app

EXPOSE 8007

# Comando para rodar o servidor FastAPI com Uvicorn usando o Python do venv
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8007"]
