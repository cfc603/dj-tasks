=====
Usage
=====

``dj_tasks`` provides a parent ``Task`` that all declared tasks should inherit from. It includes two required attributes ``name`` and ``frequency``, where ``name`` is how it will be displayed in the standard output of the management command and ``frequency`` is how often it should run in seconds. Finally, it must override the ``run`` method which will provide the task functionality.

.. code-block:: python

    # your_app/tasks.py
    from dj_tasks.tasks import Task

    class MyTask(Task):

        name = "My Custom Task"
        frequency = 20

        def run(self):
            print(f"{self.name} that runs every {self.frequency} seconds.")


In your project ``settings.py`` declare your new task.

.. code-block:: python

    DJTASKS_LOCK_ID = "your_django_project"
    DJTASKS_TASKS = [
        "your_app.tasks.MyTask",
    ]

At the command line:

    ``$ python manage.py run_tasks``
