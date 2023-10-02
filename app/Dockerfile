# Используйте официальный образ Python
FROM python:3.9

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

# Копируйте исходный код FastAPI-приложения в контейнер
COPY . ./app/

# Установите рабочую директорию
WORKDIR /app

# Запустите FastAPI приложение с помощью Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
