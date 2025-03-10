Сервис для управления статьями и комментариями
=====

Описание проекта
----------

Проект представляет собой cистемe управления статьями и комментариями с поддержкой вложенных обсуждений. API поддерживает операции добавления и получения комментариев к статьям и другим комментариям, а также позволяет получать древовидную структуру комментариев.

Проект разворачивается в трех Docker контейнерах: web-приложение, postgresql-база данных и nginx-сервер.

В проекте реализована аутентификация на базе токенов, настроена админка.

Настроены пермишены и пагинации для эндпоинтов. 

Приготовлены фикстуры для звполнения БД тестовыми данными (пароль и никнейм админа в фикстурах БД - ```admin```).

Системные требования
----------
* Python 3.8+
* Docker
* Works on Linux

Стек технологий
----------
* Python 3.8+
* Django 3.1
* Django Rest Framework
* PostreSQL
* Nginx
* gunicorn
* Docker, Docker Compose

Установка проекта из репозитория
----------
1. Клонирование репозитория:
```bash 
git clone git@github.com:NikitaChalykh/comment_system_service.git

cd comment_system_service
```

2. Создайте файл ```.env``` используя ```env.example``` в качестве шаблона в папке infra

3. Установка и запуск приложения в контейнерах:
```bash 
docker-compose up -d
```

4. Запуск миграций, сбор статики и загрузка фикстур:
```bash 
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py collectstatic --no-input 

docker-compose exec web python manage.py loaddata fixtures.json
```

Работа с проектом
----------
Документация по работе API сервиса:

```http://127.0.0.1/redoc/```

```http://127.0.0.1/swagger/```

Админка сервиса:

```http://127.0.0.1/admin/```
