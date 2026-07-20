FROM python:3.11-slim

WORKDIR /app

# Устанавливаем системные зависимости напрямую из репозиториев Debian
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        # В Debian за работу с источниками ПО отвечает пакет ca-certificates,
        # он нужен для HTTPS-запросов pip и wget. Утилита add-apt-repository здесь не требуется.
        ca-certificates \
        # Если вам нужна возможность добавлять сторонние APT-репозитории вручную,
        # установите gnupg (для проверки подписей) и lsb-release (для определения версии ОС)
        gnupg \
        lsb-release && \
    rm -rf /var/lib/apt/lists/*

# сначала копируем только requirements.txt и устанавливаем зависимости
COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt

# Затем копируем остальной код
COPY . /app

CMD ["python3", "ServiceApp.py"]