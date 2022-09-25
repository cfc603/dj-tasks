# -*- coding: utf-8 -*-

import socket
import sys
import time

from django.core.management.base import BaseCommand
from django.db import connection

from dj_tasks import settings as dj_tasks_settings
from dj_tasks.utils import get_class


class Command(BaseCommand):

    help = "run all specified tasks in dj_tasks_settings.DJTASKS_TASKS"

    def add_arguments(self, parser):
        parser.add_argument(
            "--production",
            action="store_true",
            dest="production",
            default=False,
            help="Specify when on production server.",
        )

    def get_lock_id(self):
        if dj_tasks_settings.DJTASKS_LOCK_ID:
            return dj_tasks_settings.DJTASKS_LOCK_ID
        raise NotImplementedError("Specify DJTASKS_LOCK_ID in settings")

    def get_tasks(self):
        tasks = []
        for task in dj_tasks_settings.DJTASKS_TASKS:
            tasks.append(get_class(task))
        return tasks

    def handle(self, *args, **options):
        if dj_tasks_settings.DJTASKS_LOCK:
            if not self.is_lock_free(options["production"]):
                sys.exit()

        while True:
            for Task in self.get_tasks():
                task = Task(self.output)
                try:
                    task.full_run()
                except Exception as e:
                    msg = f"Error occurred while running task {task.name}: {e}"
                    self.output(msg, "WARNING")

            # clone database connection
            connection.close()
            self.output("Database connection closed.")

            # no need to run more frequently than the tasks require
            time.sleep(dj_tasks_settings.DJTASKS_SLEEP_INTERVAL)

    def is_lock_free(self, production):
        global lock_socket
        lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

        lock_id = self.get_lock_id()
        if production:
            lock_id += ".production"

        try:
            lock_socket.bind("\0" + lock_id)
            self.stdout.write(
                self.style.SUCCESS(f"Acquired lock {lock_id}\n")
            )
            return True
        except socket.error:
            # socket already locked, task must already be running
            self.stdout.write(
                self.style.WARNING("Failed to acquire lock\n")
            )
            return False

    def output(self, message, style="SUCCESS"):
        style = getattr(self.style, style)
        self.stdout.write(style(message))
