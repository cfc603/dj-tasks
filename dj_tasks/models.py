# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

from model_utils.models import TimeStampedModel


class Task(TimeStampedModel):

    name = models.CharField(max_length=120, unique=True)
    frequency = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_last_run(self):
        return self.taskrun_set.order_by("-created").first()

    def run_again(self):
        last_run = self.get_last_run()
        if last_run:
            last_run_time = last_run.created
            next_run_time = last_run_time + timezone.timedelta(
                seconds=self.frequency
            )
            return next_run_time <= timezone.now()
        return True


class TaskRun(TimeStampedModel):

    task = models.ForeignKey("Task", on_delete=models.CASCADE)
