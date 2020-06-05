=============================
dj-tasks
=============================

.. image:: https://badge.fury.io/py/dj-tasks.svg
    :target: https://badge.fury.io/py/dj-tasks

.. image:: https://travis-ci.org/cfc603/dj-tasks.svg?branch=master
    :target: https://travis-ci.org/cfc603/dj-tasks

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

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
