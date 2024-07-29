# Тестовое заданиe 
##Реализовано:
     1. Bacend-часть приложения для управления задачами (To-Do List)
     2. Методы для создания, редактирования, отображения, удаления записей
     3. Пагинация при отображении всех задач
     4. Фильтрация задач по параметру completed=True|False
     5. Валидация данных

## Требования

- Python 3.8 или новее
- pip
- virtualenv (рекомендуется)
- PostgreSQL(>=13)

## Установка

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/ThreeToads/To-Do-List.git
    cd To-Do-List
    ```

2. **Создайте виртуальное окружение:**

    ```bash
    python -m venv venv
    ```

3. **Активируйте виртуальное окружение:**

    - На Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - На macOS и Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

## Настройка

1.**Создайте файл `.env` по подобию `.env.example` в том же месте:**

2.**Создайте базу данных PostgreSQL и внесите данные о ней в `.env` файл**


3.**Примените миграции базы данных:**

    ```bash
    python manage.py migrate
    ```

4.**Создайте суперпользователя:**

    ```bash
    python manage.py createsuperuser
    ```

## Запуск

1. **Запустите сервер разработки:**

    ```bash
    python manage.py runserver
    ```

2. **Откройте браузер и перейдите по адресу:**

    ```
    http://127.0.0.1:8000/swagger/
    http://127.0.0.1:8000/admin/
    ```

## Тестирование

1. **Swagger:**

    - используя имя и пароль суперпользователя
   через api/login получите aссess токен
    - введите его в Available authorizations(Authorize)
    - протестируйте методы
   

2. **Postman:**
    - Зайдите на сайт `https://web.postman.co/`
    - создайте новое workflow
    - протестируйте методы, введя в поле `Bearer Token` токен access

## Лицензия

Этот проект лицензирован под MIT License. Подробности см. в файле [LICENSE](LICENSE).

## Авторы

- [Кокин Иван](https://github.com/ThreeToads)

