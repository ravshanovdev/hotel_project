from celery import Celery
from celery.schedules import crontab
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete': {
        'task': 'accounts.tasks.account_delete_task.get_users',
        'schedule': crontab(hour=0, minute=0),
    },
}
