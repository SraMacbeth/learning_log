from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Apply migrations and collect static files'

    def handle(self, *args, **kwargs):
        self.stdout.write('Applying migrations...')
        call_command('migrate')
        self.stdout.write('Collecting static files...')
        call_command('collectstatic', '--noinput')
        self.stdout.write('Done!')
