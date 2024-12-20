import pytest, requests

@pytest.fixture
def get_response():
    resp = requests.get('http://127.0.0.1:5000/greet/IITM')
    return resp
def test_response():
    resp = requests.get('http://127.0.0.1:5000/greet/IITM')
    assert resp.text == 'Hello, IITM'

