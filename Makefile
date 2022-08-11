install:  ## Install package from source in edit mode
	pip install -e .

deps:  ## Install development dependencies
	pip install -r requirements.txt

lint:  ## Lint code
	flake8 --config flake8 google_serp_api/ setup.py

build:  ## Build a binary wheel and a source tarball
	python setup.py sdist bdist_wheel
