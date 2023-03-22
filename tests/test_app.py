import pytest

from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_app_post(client):
    response = client.post('/', data={"animal": "Camel"})
    assert response.status_code == 302


def test_app_get(client):
    response = client.get('/')
    assert response.status_code == 200
