from django.core.management.base import BaseCommand, CommandError
from phone_form.update_db_task import update_data

class Command(BaseCommand):
    help = 'Runs the update_data Celery task on startup'

    def handle(self, *args, **options):
        try:
            update_data.delay()
            self.stdout.write(self.style.SUCCESS('Task update_data queued for execution.'))
        except Exception as e:
            raise CommandError(f'Error running task: {e}')