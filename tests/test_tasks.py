#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dj-tasks
------------

Tests for `dj-tasks` tasks module.
"""
from unittest.mock import Mock, patch

from django.test import TestCase
from django.utils import timezone

from model_bakery import baker

from dj_tasks.models import Task as TaskModel, TaskRun
from dj_tasks.tasks import Task, DeleteOldTaskRunTask


class TestDj_tasks(TestCase):

    @patch("dj_tasks.tasks.TaskRun")
    @patch("dj_tasks.tasks.Task.get_instance")
    @patch("dj_tasks.tasks.Task.run")
    def test_full_run_if_run_again(self, mock_run, mock_get_instance,
                                   MockTaskRun):
        # setup
        instance = Mock(
            run_again=Mock(return_value=True)
        )
        mock_get_instance.return_value = instance

        task = Task(Mock())
        task.name = "Test Name"
        task.full_run()

        # asserts
        mock_run.assert_called_once()
        MockTaskRun.objects.create.assert_called_once_with(task=instance)

    @patch("dj_tasks.tasks.Task.get_instance")
    @patch("dj_tasks.tasks.Task.run")
    def test_full_run_if_not_run_again(self, mock_run, mock_get_instance):
        # setup
        mock_get_instance.return_value = Mock(
            run_again=Mock(return_value=False)
        )

        task = Task(Mock())
        task.full_run()

        # asserts
        mock_run.assert_not_called()

    def test_get_frequency_if(self):
        # setup
        task = Task(Mock())
        task.frequency = 5

        # asserts
        self.assertEqual(task.get_frequency(), 5)

    def test_get_frequency_if_not(self):
        # setup
        task = Task(Mock())

        # asserts
        with self.assertRaises(NotImplementedError):
            task.get_frequency()

    def test_get_instance_created(self):
        # setup
        task = Task(Mock())
        task.name = "Test Name"
        task.frequency = 5

        task_instance = task.get_instance()
        tasks = TaskModel.objects.all()

        # asserts
        self.assertEqual(tasks.count(), 1)
        self.assertEqual(tasks.first(), task_instance)
        self.assertEqual(task_instance.name, "Test Name")
        self.assertEqual(task_instance.frequency, 5)

    def test_get_instance_not_created(self):
        # setup
        baker.make(TaskModel, name="Test Name")

        task = Task(Mock())
        task.name = "Test Name"
        task.frequency = 5

        task_instance = task.get_instance()
        tasks = TaskModel.objects.all()

        # asserts
        self.assertEqual(tasks.count(), 1)
        self.assertEqual(tasks.first(), task_instance)
        self.assertEqual(task_instance.name, "Test Name")
        self.assertEqual(task_instance.frequency, 5)

    def test_get_name_if(self):
        # setup
        task = Task(Mock())
        task.name = "name"

        # asserts
        self.assertEqual(task.get_name(), "name")

    def test_get_name_if_not(self):
        # setup
        task = Task(Mock())

        # asserts
        with self.assertRaises(NotImplementedError):
            task.get_name()

    def test_run(self):
        # setup
        task = Task(Mock())

        # asserts
        with self.assertRaises(NotImplementedError):
            task.run()


class TestDeleteOldTaskRunTask(TestCase):

    def test_run(self):
        # setup
        now = timezone.now()

        days = [15, 16, 13, 1]
        all_runs = []
        for day in days:
            task_run = baker.make(TaskRun)
            task_run.created = now - timezone.timedelta(days=day)
            task_run.save()
            all_runs.append(task_run)

        DeleteOldTaskRunTask(Mock()).run()

        task_runs = TaskRun.objects.all()

        # asserts
        self.assertEqual(task_runs.count(), 2)
        self.assertIn(all_runs[1], all_runs)
        self.assertIn(all_runs[2], all_runs)
