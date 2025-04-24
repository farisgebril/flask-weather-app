import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_weather_endpoint(client):
    response = client.get('/weather/london')
    assert response.status_code == 200
