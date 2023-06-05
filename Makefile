.PHONY: test

install:
	pip3 install --upgrade pip &&\
		pip3 install pytest pylint pytest-cov black

test:
	python3 -m pytest -vv --cov=app test_ml_app.py

format:
	black *.py

lint:
	pylint --disable=R,C,W1203,W0703 app.py

build: 
	sudo docker build -t aws_ml_app -f docker/Dockerfile .

run: 
	sudo docker run -p 8080:8080 aws_ml_app
	
all: install test format lint build run