from fastapi.testclient import TestClient
from app import app
import pytest
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class Item(BaseModel):
    message: str


client = TestClient(app)


def test_index():
    """Test the index route."""
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
