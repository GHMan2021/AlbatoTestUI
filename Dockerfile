FROM python:3.11-slim-bookworm

WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget curl unzip gnupg2 ca-certificates \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libxkbcommon0 \
    libxcomposite1 libxdamage1 libxrandr2 libgbm1 libasound2 \
    libxshmfence1 libxss1 libgtk-3-0 libx11-xcb1 libxext6 libdrm2 \
    libxcb1 libxcb-dri3-0 libxfixes3 \
    && rm -rf /var/lib/apt/lists/*

# Установка JDK (для Allure CLI)
RUN mkdir -p /etc/apt/keyrings \
    && wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor -o /etc/apt/keyrings/adoptium.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/adoptium.gpg] https://packages.adoptium.net/artifactory/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" > /etc/apt/sources.list.d/adoptium.list \
    && apt-get update && apt-get install -y --no-install-recommends temurin-21-jdk \
    && rm -rf /var/lib/apt/lists/*

# Установка Allure CLI
RUN wget -q https://github.com/allure-framework/allure2/releases/download/2.34.0/allure-2.34.0.zip -O /tmp/allure.zip \
    && unzip /tmp/allure.zip -d /opt/ \
    && ln -s /opt/allure-2.34.0/bin/allure /usr/local/bin/allure \
    && rm /tmp/allure.zip

# Установка Python-зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Установка Playwright и браузеров
RUN pip install --no-cache-dir playwright \
    && playwright install --with-deps

# Копируем проект
COPY . /app
