from django.core.management.base import BaseCommand
import os, shutil
from django.db import connection

MIGRATIONS_DIR = "./askPupkin_models/migrations"

class Command(BaseCommand):
    def handle(self, *args, **options):
        shutil.rmtree(MIGRATIONS_DIR, ignore_errors=True)
        with connection.cursor() as cursor:
            cursor.execute("drop database askpupkin_db;")
            cursor.execute("create database askpupkin_db;")
        os.system("manage.py makemigrations askPupkin_models")
        os.system("manage.py migrate")
        os.system("manage.py fill_db 2")
        
