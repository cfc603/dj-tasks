# -*- coding: utf-8 -*-

from django.utils import timezone

from dj_tasks import settings as dj_tasks_settings

from .models import Task as TaskModel, TaskRun


class Task:

    name = None
    frequency = None

    def __init__(self, output):
        self.output = output

    def full_run(self):
        instance = self.get_instance()
        if instance.run_again():
            self.output(f"Running {self.get_name()}")
            self.run()
            TaskRun.objects.create(task=instance)
            self.output(f"Completed {self.get_name()}\r")

    def get_frequency(self):
        if self.frequency:
            return self.frequency
        raise NotImplementedError("Every task needs a frequency.")

    def get_instance(self):
        task, c = TaskModel.objects.update_or_create(
            name=self.get_name(), defaults={"frequency": self.get_frequency()}
        )
        return task

    def get_name(self):
        if self.name:
            return self.name
        raise NotImplementedError("Every task needs a name.")

    def run(self):
        raise NotImplementedError("Every task needs a run method.")


class DeleteOldTaskRunTask(Task):

    name = "Delete old TaskRun entries"
    frequency = 60 * 60 * 24  # daily

    def run(self):
        interval = timezone.timedelta(
            days=dj_tasks_settings.DJTASKS_DELETE_INTERVAL
        )
        task_runs = TaskRun.objects.filter(created__lte=timezone.now() - interval)
        if task_runs.exists():
            task_runs.delete()
