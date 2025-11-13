FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl gcc && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry==1.8.0

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only main

COPY app/backend ./app/backend

COPY data/models ./data/models

EXPOSE 5000

CMD ["uvicorn", "app.backend.main:app", "--host", "0.0.0.0", "--port", "5000"]