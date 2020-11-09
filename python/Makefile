##
#
#
#
#
#
#


all:
	@echo "No all - see build, test, run, lint

lint:
	@echo "Linting with flake8"
	flake8

build:
	@echo "Nothing to build - it's python"

test:
	python3 -m unittest discover ./tests/ "test_*.py"

vtest:
	python3 -m unittest discover -v ./tests/ "test_*.py"

run:
	@echo "Running -"
	python3 test.py

coverage:
	coverage run -m unittest discover ./tests/ "test_*.py"
	coverage report -m

htmlcov: coverage
	coverage html

viewcoverage: htmlcov
	x-www-browser htmlcov/index.html

clean:
	rm -f *.pyc
	rm -rf htmlcov