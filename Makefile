.PHONY: test

install:
	pip install --upgrade pip &&\
		pip install pytest pylint pytest-cov black

test:
	python -m pytest -vv --cov=app test_ml_app.py

format:
	black *.py

lint:
	pylint --disable=R,C,W1203,W0703 app.py

build: 
	docker build -t aws_ml_app -f docker/Dockerfile .

run: 
	docker run -p 127.0.0.1:8080:8080 aws_ml_app
	
all: install test format lint build run