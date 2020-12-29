# -*- coding: utf-8 -*-


from unittest.mock import Mock, call, patch

from django.test import TestCase

from dj_tasks.tasks import Task, DeleteOldTaskRunTask
from dj_tasks.management.commands.run_tasks import Command


class CommandTest(TestCase):

    def test_get_lock_id_if(self):
        # setup
        command = Command()

        # asserts
        self.assertEqual(command.get_lock_id(), "123456")

    def test_get_tasks(self):
        # setup
        command = Command()

        # asserts
        self.assertEqual(command.get_tasks(), [Task, DeleteOldTaskRunTask])

    def test_output(self):
        # setup
        stdout = Mock()

        command = Command()
        command.stdout = stdout
        command.output("Test Message")

        # asserts
        stdout.write.assert_called_once_with(
            command.style.SUCCESS("Test Message")
        )

    def test_output_style_change(self):
        # setup
        stdout = Mock()

        command = Command()
        command.stdout = stdout
        command.output("Test Message", "WARNING")

        # asserts
        stdout.write.assert_called_once_with(
            command.style.WARNING("Test Message")
        )
