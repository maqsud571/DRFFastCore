# FROM python:3.9

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# WORKDIR /app

# # requirements.txt ni nusxalash va o'rnatish
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# # loyihani nusxalash
# COPY . .

# # Skriptga ijro huquqini berish
# RUN chmod +x str/django.sh

# EXPOSE 8000

# # Konteyner ishga tushganda skriptni ishga tushuradi
# ENTRYPOINT ["str/django.sh"]
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Django loyihasi konteyner ichida
WORKDIR /app/str

# requirements o'rnatish
COPY requirements.txt .
RUN pip install -r requirements.txt

# loyihani nusxalash
COPY . .

EXPOSE 8000

# Server ishga tushishi
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["str/django.sh"]