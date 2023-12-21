import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_NAME = os.getenv('DATABASE_NAME')

    DJANGO_TIME_ZONE = os.getenv('DJANGO_TIME_ZONE')
    DJANGO_SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
