## Проект UI автотестов сервиса Swag Labs

### Установка окружения и запуск тестов

1. Установка приложений:

    * Для linux пользователей установите [Docker](https://docs.docker.com/engine/install/)

    * Для windows пользователей установите [Docker](https://docs.docker.com/desktop/windows/install/)

2. Склонировать репозиторий
```
git clone https://github.com/GHMan2021/AlbatoTestUI.git
```
3. Перейти в директорию проекта
4. Переименовать файл ".env.example" в ".env"
5. Выполнить команду на сбор проекта и запуск тестов
```
docker compose up --build
```
5. Просмотр в браузере Allure отчета по адресу http://localhost:4040
6. Остановка Allure server комбинацией "Ctrl+C" 

