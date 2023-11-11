from django.core.management.base import BaseCommand
import os, shutil
from django.db import connection

MIGRATIONS_DIR = "./askPupkin_models/migrations"

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'ratio',
            nargs='?',
            type=int,
        )

    def handle(self, *args, **options):
        try: ratio = options["ratio"]
        except: ratio = 3
        shutil.rmtree(MIGRATIONS_DIR, ignore_errors=True)
        with connection.cursor() as cursor:
            cursor.execute("drop database askpupkin_db;")
            cursor.execute("create database askpupkin_db;")
        os.system("manage.py makemigrations askPupkin_models")
        os.system("manage.py migrate")
        os.system(f"manage.py fill_db {ratio}")
        
