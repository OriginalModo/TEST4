import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TESTS5.settings')

app = Celery('TESTS5')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()