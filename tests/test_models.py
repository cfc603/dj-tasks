#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dj-tasks
------------

Tests for `dj-tasks` models module.
"""
from unittest.mock import patch

from django.test import TestCase
from django.utils import timezone

from model_bakery import baker


class TestDj_tasks(TestCase):

    def test_str(self):
        # setup
        task = baker.make("dj_tasks.Task", name="Test Name")

        # asserts
        self.assertEqual(task.__str__(), "Test Name")

    def test_get_last_run(self):
        # setup
        task = baker.make("dj_tasks.Task")

        baker.make("dj_tasks.TaskRun", task=task)
        expected_run = baker.make("dj_tasks.TaskRun", task=task)

        # asserts
        self.assertEqual(task.get_last_run(), expected_run)

    def test_run_again_true(self):
        # setup
        task = baker.make("dj_tasks.Task", frequency=5)

        task_run = baker.make("dj_tasks.TaskRun", task=task)
        task_run.created = timezone.now() - timezone.timedelta(seconds=6)
        task_run.save()

        # asserts
        self.assertTrue(task.run_again())

    def test_run_again_true_no_last_run(self):
        # setup
        task = baker.make("dj_tasks.Task", frequency=5)

        # asserts
        self.assertTrue(task.run_again())

    def test_run_again_false(self):
        # setup
        task = baker.make("dj_tasks.Task", frequency=5)
        task_run = baker.make("dj_tasks.TaskRun", task=task)

        # asserts
        self.assertFalse(task.run_again())
