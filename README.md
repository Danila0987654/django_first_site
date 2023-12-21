# Django First Project


## Table of Contents
- [Run Project](#run-project)
- [How to build PostgreSQL docker-compose](#build-postgresql-with-docker-compose)


## Run Project

Clone the project
```bash
git clone https://github.com/Danila0987654/django_first_site
```
***

Go to the project directory
```bash
cd django_first_site
```
***

Create venv, activate it and upgrade pip:
```bash
python3 -m venv venv
. ./venv/bin/activate
pip install -U pip
```
***

Install dependencies:
```bash
pip install -r requirements.txt
```
***

Create .env file and input data with your information:

    DATABASE_PORT=
    DATABASE_USER=
    DATABASE_PASSWORD=
    DATABASE_NAME=
    DJANGO_SECRET_KEY=

If you aren't using a postgresql, then change settings in 
mysite/settings.py
***

Run Django Server
```bash
python manage.py runserver
```

[Return](#table-of-contents)


## Build PostgreSQL with docker-compose

Build docker-compose

```bash
docker-compose up -d
```

[Return](#table-of-contents)

