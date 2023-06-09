[![Deploy to AWS EC2](https://github.com/mmmarchetti/AWSAppMLOpsTemplate/actions/workflows/main.yml/badge.svg)](https://github.com/mmmarchetti/AWSAppMLOpsTemplate/actions/workflows/main.yml)
# AWS MLOps CI/CD Template

This template provides a pre-configured set of files and scripts to help you quickly create a Python Machine Learning Fast API, containerize it using Docker, and continuously deploy it on AWS using Elastic Beanstalk and GitHub Actions.

What's Included

* Dockerfile to build Docker image for your Fast API.
* Makefile with commands to install dependencies, lint, test, build, and run your Fast API.
* GitHub Actions workflow (main.yml) for continuous integration and deployment.

# Testing the Basic API

This guide will walk you through testing the basic API functionality for this project. We will use the interactive API documentation provided by FastAPI.

**API Base URL**: http://awsmlapp-env.eba-22wzt6z2.us-east-1.elasticbeanstalk.com/

1. **Access the API Documentation**

    Open your preferred web browser and navigate to the `/docs` endpoint of the base URL:

    ```
    http://awsmlapp-env.eba-22wzt6z2.us-east-1.elasticbeanstalk.com/docs
    ```

    This will open up the FastAPI's interactive Swagger UI documentation for the API.

2. **Testing the Endpoints**

    The interactive documentation provides a list of all available API endpoints. Here is how you can test them:

    - **GET /**: Click on the GET request listed under "Default". Then, click on the "Try it out" button, followed by the "Execute" button. You should see the "API is Working!" message in the "Response body".

    - **POST /echo**: Click on the POST request listed under "Default". Click on "Try it out". In the "Request body" field that appears, input a JSON object with a key-value pair where the key is `message`. For example: 
        ```json
        {
            "message": "Hello, World!"
        }
        ```
        Click "Execute". In the "Response body", you should see the echo of your message.

Remember, this is a basic API and mainly intended to be used as a template for further development. You can add your machine learning models and build more complex API endpoints using this as a starting point.

# Using this Template

## Setup and Configuration

1. AWS Configuration
Ensure you have an AWS account and your AWS credentials (Access Key ID and Secret Access Key) are set up either in your environment variables or AWS credentials file.

2. Amazon ECR
Create an Amazon Elastic Container Registry (ECR) repository where your Docker images will be pushed. Note down the repository name.

3. AWS Elastic Beanstalk
Create an Elastic Beanstalk environment with a Docker platform. The environment URL is provided in the Elastic Beanstalk console.

4. GitHub Secrets
In your GitHub repository, go to Settings -> Secrets and add the following secrets:

AWS_ACCESS_KEY_ID: Your AWS access key ID.
AWS_SECRET_ACCESS_KEY: Your AWS secret access key.

5. Modify GitHub Actions Workflow
In main.yml, update the following environment variables:

AWS_REGION: The AWS region where your ECR repository and Elastic Beanstalk environment are located.
ECR_REPOSITORY: The name of your ECR repository.
EB_ENVIRONMENT: The name of your Elastic Beanstalk environment.

6. Run the Application
Push to the main branch of your repository to trigger the GitHub Actions workflow. The workflow will install dependencies, run linting and tests, build the Docker image, push the image to your ECR repository, and deploy the application to your Elastic Beanstalk environment.

Access the Application

Once deployed, you can access the application by navigating to the URL of your Elastic Beanstalk environment.

This template is designed to help you get started quickly with FAST API, Docker, AWS ECR, and Elastic Beanstalk. However, you may need to make modifications based on the specifics of your project. Happy coding!

### Project Structure
```
project_name/
|
|__ app.py                              - FAST API app python file
|
|__ data/ 
|    |
|    |__ raw/                           - Raw, unprocessed data
|    |   |__ dataset.csv
|    |
|    |__ interim/                       - Intermediate data after some preprocessing
|    |   |__ cleaned_data.csv
|    |
|    |__ processed/                     - Final data used for modeling
|    |   |__ preprocessed_data. csv
|    |
|    |__ external/                      - Data from external sources
|        |__ external_data. csv
|
|__ trained_models/                     - Trained and serialized models
|    |__model_v1.pk
|
|__ notebooks/                          - Jupyter notebooks for exploration and analysis
|    |__exploratory_analysis.ipynb
|
|__ src/ 
|    |                                  - Source code for the project 
|    |__ data/                          - Scripts to download, preprocess and generate data
|    |   |__ download_data.py                 
|    |   |__ preprocess_data.py
|    |
|    |__ features/                      - Scripts to turn raw data into features for modeling
|    |   |__ feature_engineering.py
|    |
|    |__ models/                        - Scripts to train models and make predictions
|    |   |__ train_model.py 
|    |   |__ predict_model.py
|    |
|    |__ visualization/                 - Scripts to create visualizations
|    |   |__ visualize_data.py
|    |
|    |__ reports/                       
|        |
|        |__ figures/                   - Generated graphics and figures  
|        |   |__ histogram.png
|        |  
|        |__ docs                       - Generated analysis as HTML, PDF, or other formats
|            |__ report.pdf            
|
|__ docker/                             - Docker files
|    |__ Dockerfile                 
|                            
|__ test_app.py                      - Create Automated Test scripts using pytest
|
|__ .gitignore                          - List of files and directories to ignore in version cont
|
|__ README.md                           - Project description and setup guide
|
|__ requirements.txt                    - Python dependencies for the project
|
|__ .env                                - Env secrets (KEYS, passwords, etc...) Obs. Listed in .gitignore
|
|__ Makefile                            - Make file for CI/CD
|
|__ .github/worflows                    - GitHub Actions for automated CI/CD in aws
```
