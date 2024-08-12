import pytest
import requests
from unittest import mock
from utils.helper import get_neo_feed, get_apod
from requests.exceptions import Timeout

class TestEdgeCases:
    def test_unexpected_api_response(self):
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {"unexpected_key": "unexpected_value"}

            response = get_neo_feed("2023-07-01", "2023-07-07")
            data = response.json()

            assert 'near_earth_objects' not in data

    def test_rate_limiting(self):
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 429
            response = get_neo_feed("2023-07-01", "2023-07-07")

            assert response.status_code == 429