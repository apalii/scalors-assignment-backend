from __future__ import absolute_import, unicode_literals
import requests
from celery import shared_task, Celery, task

celery = Celery('tasks', broker='amqp://guest@localhost//')


@shared_task
def send_reminder(reminder_text):
    result = requests.post("localhost:8000/test", data={'reminder': reminder_text})
    return result.responce_code
