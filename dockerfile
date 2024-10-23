# Etapa 1: Builder
FROM python:3.12.3-slim AS builder

WORKDIR /app

# Instala pacotes de sistema necessários
RUN apt-get update && apt-get install -y build-essential libpq-dev curl

# Instala o Poetry
RUN pip install poetry

# Copia os arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock README.md /app/

# Configura o Poetry para criar o virtualenv dentro do projeto
RUN poetry config virtualenvs.in-project true

# Instala as dependências no ambiente virtual
RUN poetry install --no-dev --no-interaction --no-ansi

# Etapa 2: Imagem final
FROM python:3.12.3-slim

WORKDIR /app

# Copia o projeto e as dependências da primeira etapa
COPY --from=builder /app /app

# Define a variável de ambiente para o Python do venv
ENV PATH="/app/.venv/bin:$PATH"

# Copia o código restante
COPY . /app

EXPOSE 8007

# Comando para rodar o servidor FastAPI com Uvicorn
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8007"]
