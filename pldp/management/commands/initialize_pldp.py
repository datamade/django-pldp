import os

from django.core.management.base import BaseCommand, CommandError
from django.core import management

from languages_plus import models as language_models

LANGUAGE_FIXTURE_DIR = os.path.join(os.path.abspath(os.path.dirname(language_models.__file__)), 'fixtures')

class Command(BaseCommand):
    help = 'Loads fixtures needed for PLDP'

    def handle(self, *args, **options):
        self.stdout.write(self.style.HTTP_INFO('Loading languages ....\n'))
        language_fixture_path = os.path.join(LANGUAGE_FIXTURE_DIR, 'languages_data.json.gz')
        management.call_command('loaddata', language_fixture_path)

        self.stdout.write(self.style.HTTP_INFO('Loading countries ....\n'))
        management.call_command('update_countries_plus')
        self.stdout.write(self.style.SUCCESS('PLDP models initialized!'))
