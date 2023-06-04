import pytest
from app import app as flask_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    return flask_app


@pytest.fixture
def client(app):
    """Provide a test client for the app"""
    return app.test_client()


def test_index(client):
    """Test the index route."""
    res = client.get("/")
    assert res.status_code == 200
    expected = "<h3>Working!</h3>"
    assert expected in res.get_data(as_text=True)
