install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt

format:
		black *.py

lint:
		pylint --disable=R,C script.py

test:
		python3 -m pytest test_*.py

all: install format lint test