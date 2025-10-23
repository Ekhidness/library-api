# REST API для электронной библиотеки

Этот проект представляет собой REST API для управления электронной библиотекой. Позволяет просматривать книги и авторов, а также администраторам добавлять новые книги.

## Установка и запуск

1.  Клонируйте репозиторий.
2.  Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    # Windows: venv\Scripts\activate
    # macOS/Linux: source venv/bin/activate
    ```
3.  Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
4.  Выполните миграции:
    ```bash
    python manage.py migrate
    ```
5.  Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```
6.  Запустите сервер:
    ```bash
    python manage.py runserver
    ```

## Эндпоинты API

*   `GET /api/authors/` — Список всех авторов.
*   `GET /api/authors/<id>/` — Информация об авторе.
*   `GET /api/books/` — Список всех книг.
*   `GET /api/books/<id>/` — Информация о книге.
*   `POST /api/books/create/` — Создать книгу (требуется авторизация админа).
*   `GET /api/books/search/?q=<query>` — Поиск книг.

## Примеры запросов (curl)

Получить список книг:
```bash
curl http://127.0.0.1:8000/api/books/
