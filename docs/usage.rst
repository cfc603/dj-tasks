=====
Usage
=====

To use dj-tasks in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_tasks.apps.DjTasksConfig',
        ...
    )

Add dj-tasks's URL patterns:

.. code-block:: python

    from dj_tasks import urls as dj_tasks_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_tasks_urls)),
        ...
    ]
