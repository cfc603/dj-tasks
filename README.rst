=============================
dj-tasks
=============================

.. image:: https://badge.fury.io/py/dj-tasks.svg
    :target: https://badge.fury.io/py/dj-tasks

.. image:: https://github.com/cfc603/dj-tasks/workflows/Django%20CI/badge.svg
    :target: https://github.com/cfc603/dj-tasks/actions

.. image:: https://codecov.io/gh/cfc603/dj-tasks/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/cfc603/dj-tasks

A django app to run a collection of tasks in a management command.

Documentation
-------------

The full documentation is at https://dj-tasks.readthedocs.io.

Quickstart
----------

Install dj-tasks::

    pip install dj-tasks

Add it to your ``INSTALLED_APPS``:

.. code-block:: python

    # project/settings.py
    INSTALLED_APPS = [
        ...
        'dj_tasks',
        ...
    ]

Create a task:

.. code-block:: python

    # your_app/tasks.py
    from dj_tasks.tasks import Task


    class YourTask(Task):

        name = "Your Task"
        frequency = 60

        def run(self):
            print("Your custom code...")

Add to your ``DJTASKS_TASKS`` settings:

.. code-block:: python

    # project/settings.py
    DJTASKS_LOCK_ID = "your_django_project"
    DJTASKS_TASKS = [
        "your_app.tasks.YourTask",
    ]


Running Tests
-------------

Does the code actually work?

::

    $ make install-dev
    $ make lint
    $ make test


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
