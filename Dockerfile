FROM python:3.10.12

ENV PYTHONUNBUFFERED 1

# pg_isready uchun
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY django.sh /django.sh
RUN chmod +x /django.sh

COPY str/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
