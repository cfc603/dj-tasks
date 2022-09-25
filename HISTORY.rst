.. :changelog:

History
-------

2.0.0 (2022-09-25)
++++++++++++++++++

* handle exception when running individual tasks
* Drop support for django <3.2
* Add support for django 4.0 and 4.1

1.1.0 (2020-12-28)
++++++++++++++++++

* add documentation of ``DJTASKS_LOCK_ID`` to Quickstart
* update MakeFile to use current work flow
* close database connection after each full run
* add dj_tasks.tasks.DeleteOldTaskRunTask
* flake8 fixes
* add twine for easier releases
* move to GitHub Actions from Travis CI
* drop testing with tox

1.0.0 (2020-07-01)
++++++++++++++++++

* require setting ``DJTASKS_LOCK_ID``

0.1.0 (2020-06-05)
++++++++++++++++++

* First release on PyPI.
