# Django First Project


## Table of Contents
- [How to build PostgreSQL](#build-postgresql)
- [Run Django server](#run-django-server)


## Build PostgreSQL
Clone the project

```bash
git clone https://github.com/Danila0987654/django_first_site
```

Go to the project directory

```bash
cd django_first_site
```

Create .env file and input data with your information:

***
    POSTGRES_PORT=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB=
***

Build docker-compose

```bash
docker-compose up -d
```

[Return](#table-of-contents)


## Run Django Server

```bash
python manage.py runserver
```

[Return](#table-of-contents)