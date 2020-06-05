# -*- coding: utf-8 -*-

from django.conf import settings

DJTASKS_LOCK = getattr(settings, "DJTASKS_LOCK", True)

DJTASKS_SLEEP_INTERVAL = getattr(settings, "DJTASKS_SLEEP_INTERVAL", 10)

DJTASKS_TASKS = getattr(settings, "DJTASKS_TASKS", [])
