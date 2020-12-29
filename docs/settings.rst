=====
SETTINGS
=====

DJTASKS_DELETE_INTERVAL = 14
============================

Interval in days to specify how old ``dj_tasks.models.TaskRun`` entries to delete. Run daily through ``dj_tasks.tasks.DeleteOldTaskRunTask``.

DJTASKS_LOCK = True
===================

If ``True``, the management command will exit if another instance of the command is already running. This was a workaround PythonAnywhere used to offer for `Long Running Tasks <https://help.pythonanywhere.com/pages/LongRunningTasks/>`_ to ensure your task is always running, they have since switched to offering a paid feature `Always-on Tasks <https://help.pythonanywhere.com/pages/AlwaysOnTasks>`_. It's no longer documented, but it still is a valid option.

DJTASKS_LOCK_ID = ""
====================

This must be set in order to use the ``run_tasks`` management command. A good naming convention would be to use your Django project name.

DJTASKS_SLEEP_INTERVAL = 10
===========================

Specifies how long the management command ``run_tasks`` should sleep before looping through tasks specified in ``DJTASKS_TASKS``. Keep in mind if you have a ``Task.frequency = 10``, and ``DJTASKS_SLEEP_INTERVAL = 20``, your task will only run every 20 seconds.

DJTASKS_TASKS = [ ]
==================

A list of child ``Task`` that should run in the management command ``run_tasks``.
