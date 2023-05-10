import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myRobot.settings')

app = Celery('myRobot')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'my_schedule': {
        'task': 'user.tasks.user_count',
        'schedule': 60,
        'args': (),
        'kwargs': {},
    }
}