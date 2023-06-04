.PHONY: test

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=app test_ml_app.py

format:
	black *.py

lint:
	pylint --disable=R,C,W1203,E1101 app.py

build: 
	docker build -t aws_ml_app -f docker/Dockerfile .

run: 
	docker run -p 127.0.0.1:8080:8080 aws_ml_app
	
all: install lint test format build run