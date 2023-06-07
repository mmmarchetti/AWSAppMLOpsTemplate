from fastapi.testclient import TestClient
import pytest
from app import app
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class IrisFeatures(BaseModel):
    """Iris features model."""

    features: list


class Item(BaseModel):
    """Item model."""

    message: str


client = TestClient(app)


def test_root():
    """Test the root route."""
    response = client.get("/")
    assert response.status_code == 200
    expected = {"message": "API is Working!"}
    assert response.json() == expected


def test_echo():
    """Test the echo route."""
    response = client.post("/echo", json={"message": "Hello, World!"})
    assert response.status_code == 200
    expected = {"echo": "Hello, World!"}
    assert response.json() == expected


def test_train():
    """Test the train route."""
    response = client.post("/train")
    assert response.status_code == 200
    # Expected prediction is not defined, as we don't know what the model will return


def test_predict():
    """Test the predict route."""
    iris_features = {"features": [5.1, 3.5, 1.4, 0.2]}  # Example iris features
    response = client.post("/predict", json=iris_features)
    assert response.status_code == 200
    # Expected prediction is not defined, as we don't know what the model will return
