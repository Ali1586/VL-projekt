# tests/test_api.py
import requests


def test_that_country_is_US():
    url = "http://api.zippopotam.us/us/90210"
    response = requests.get(url)

    assert response.status_code == 200
    response_body = response.json()

    assert response_body["country"] == "United States"
    assert response_body["post code"] == "90210"