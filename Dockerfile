FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY Pipfile* ./

RUN python -m pip install --upgrade pip && \
    python -m pip install pipenv && \
    pipenv requirements > requirements.txt && \
    pip install -r requirements.txt

COPY . /app
EXPOSE 8000
