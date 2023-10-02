# Используйте официальный образ Python
FROM python:3.9

COPY requirements.txt /tg_bot/

RUN pip install -r /tg_bot/requirements.txt

COPY . ./tg_bot

WORKDIR /tg_bot

CMD ["python3", "bot.py"]
