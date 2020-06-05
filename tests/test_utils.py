# -*- coding: utf-8 -*-

from django.test import TestCase

from dj_tasks.utils import get_class
from dj_tasks.tasks import Task


class GetClassTest(TestCase):

    def test_get_class(self):
        # asserts
        self.assertEqual(Task, get_class("dj_tasks.tasks.Task"))
