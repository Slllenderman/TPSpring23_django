from django.core.management.base import BaseCommand
import pip
from askPupkin_managements import djenv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'name',
            nargs='?',
            type=str,
        )

    def handle(self, *args, **options):
        djenv.check_env_active()
        name = options["name"]
        pip.main(["install", name])
        
