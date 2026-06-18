FROM python:3.12-slim

WORKDIR /api

RUN mkdir -p /api/instance

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

EXPOSE 5000

ENTRYPOINT [ "sh", "./entrypoint.sh" ]