#!/usr/bin/env bash

# Make the run_docker.sh script executable by running chmod +x docker/run_docker.sh
# Aftrer that, run the script by running ./docker/run_docker.sh

# Build image
# rename the image to an appropriate name, in this case aws_ml_app
docker build -t aws_ml_app -f docker/Dockerfile .

# Run flask app in the port 8080
docker run -p 127.0.0.1:8080:8080 aws_ml_app