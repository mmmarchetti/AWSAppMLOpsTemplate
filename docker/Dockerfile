FROM python:3.8

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY requirements.txt .
COPY data/ .
COPY notebooks/ .
COPY reports/ .
COPY src/ .
COPY trained_models/ .
COPY app.py .

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
