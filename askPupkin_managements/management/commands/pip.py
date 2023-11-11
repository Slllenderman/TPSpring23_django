from django.core.management.base import BaseCommand
import pip
import os
from askPupkin_managements.djenv import REQUIREMENTS

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-i',
            '--install',
            action='store_true',
            default=False
        )
        parser.add_argument(
            '-u',
            '--uninstall',
            action='store_true',
            default=False
        )
        parser.add_argument(
            'name',
            nargs='?',
            type=str,
        )

    def handle(self, *args, **options):
        is_install = options["install"]
        is_uninstall = options["uninstall"]
        name = options["name"]
        if is_install:
            pip.main(["install", name])
            os.system(f"pip freeze > {REQUIREMENTS}")
        elif is_uninstall:
            pip.main(["uninstall", name])
            os.system(f"pip freeze > {REQUIREMENTS}")
        else: 
            pip.main(["install", name])
            os.system(f"pip freeze > {REQUIREMENTS}")
        
