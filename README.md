Comment management system with support for nested discussions
=====

Project description
----------

The project is a system for managing articles and comments with support for nested discussions. The API supports operations for adding and getting comments to articles and other comments, and also allows you to get a tree structure of comments.

The project is deployed in three Docker containers: a web application, a postgresql database, and an nginx server.

The project has token-based authentication, and an admin panel has been configured.

Permissions and pagination for endpoints have been configured.

Fixtures have been prepared for filling the database with test data (the password and nickname of the admin in the database fixtures are ```admin```).

System requirements
----------
* Python 3.8+
* Docker
* Works on Linux

Tech stack
----------
* Python 3.8+
* Django 3.1
* Django Rest Framework
* PostreSQL
* Nginx
* gunicorn
* Docker, Docker Compose

Installing the project from the repository
----------
1. Cloning the repository:
```bash
git clone git@github.com:NikitaChalykh/comment_system_service.git

cd comment_system_service
```

2. Create a ```.env``` file using ```env.example``` as a template in the infra folder

3. Installing and running the application in containers:
```bash
docker compose up -d
```

4. Run migrations, collect statics and load fixtures:
```bash

docker compose exec web python manage.py migrate

docker compose exec web python manage.py collectstatic --no-input

docker compose exec web python manage.py loaddata fixtures.json
```

Working with the project
----------
Documentation on the API service:

```http://127.0.0.1/redoc/```

```http://127.0.0.1/swagger/```

Service admin panel:

```http://127.0.0.1/admin/```