from __future__ import unicode_literals

from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(
            is_done=False)


class Dashboard(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{} : {}".format(self.name, self.pk)


class Task(models.Model):

    objects = models.Manager()
    active = ActiveManager()

    task_dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name='tasks')

    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now_add=True)

    task = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return "{} : dashboard {}".format(self.task, self.task_dashboard)


class Reminder(models.Model):
    remind_about = models.CharField(max_length=300)
    delay = models.PositiveIntegerField()

    def __str__(self):
        return "{} : {}".format(self.remind_about, self.delay)

