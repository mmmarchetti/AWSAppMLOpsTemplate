.PHONY: test

install:
	pip3 install --upgrade pip &&\
		pip3 install pytest pylint pytest-cov black fastapi uvicorn pydantic httpx

test:
	python3 -m pytest -vv --cov=app test_app.py

format:
	black *.py

lint:
	pylint --disable=R,C,W1203,W0703 app.py

build: 
	sudo docker build -t aws_ml_app -f docker/Dockerfile .

run: 
	sudo docker run -p 8080:8080 -e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} -e AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} aws_ml_app
	
all: install test format lint build run