.PHONY: clean-pyc clean-build docs help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

VIRTUALENV = $(shell which virtualenv)

ifeq ($(strip $(VIRTUALENV)),)
  VIRTUALENV = /usr/local/python3/bin/virtualenv
 endif

help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

clean: clean-build clean-pyc

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

venv: ## create virtualenv
	$(VIRTUALENV) venv

install: venv ## install requirements
	. venv/bin/activate; pip install -r requirements.txt

install-test: venv install ## install test requirements
	. venv/bin/activate; pip install -r requirements_test.txt

install-dev: venv install install-test ## instal dev requirements
	. venv/bin/activate; pip install -r requirements_dev.txt

lint: ## check style with flake8
	. venv/bin/activate; flake8 dj_tasks tests

test: venv ## run local env tests
	. venv/bin/activate; python runtests.py tests

test-all: ## run tests on every Python version with tox
	tox

coverage: venv ## run coverage
	. venv/bin/activate; coverage run --source dj_tasks runtests.py tests

htmlcov: venv ## run coverage and show html report
	. venv/bin/activate; coverage run --source dj_tasks runtests.py tests
	. venv/bin/activate; coverage report -m
	. venv/bin/activate; coverage html
	sensible-browser htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/dj-tasks.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ dj_tasks
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

release: clean ## package and upload a release
	. venv/bin/activate; python setup.py sdist upload
	. venv/bin/activate; python setup.py bdist_wheel upload

package: clean ## package
	. venv/bin/activate; python setup.py sdist bdist_wheel

package-test: clean package ## build and check new package
	. venv/bin/activate; twine check dist/*

release: clean ## package and upload a release
	. venv/bin/activate; twine upload dist/*

release-test: package-test ## upload to TestPyPi
	. venv/bin/activate; twine upload -r testpypi dist/*

github: ## open GitHub repo
	sensible-browser https://github.com/cfc603/dj-tasks
