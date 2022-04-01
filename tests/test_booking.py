import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_booking_homePage(client):
    resp = client.get('/booking')
    # Redirected using function called
    assert resp.status_code == 308


def test_booking_newBookingPage(client):
    resp = client.get('/booking/create')
    assert resp.status_code == 200
