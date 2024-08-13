from utils.helper import get_neo_feed
from unittest.mock import patch
import requests

class TestNeo:
    def test_neo_feed_success(self):
        start_date = "2023-07-01"
        end_date = "2023-07-07"
        response = get_neo_feed(start_date, end_date)

        assert response.status_code == 200
        data = response.json()
        assert 'near_earth_objects' in data

    def test_neo_feed_invalid_date(self):
        start_date = "2023-07-01"
        end_date = "invalid_date"
        response = get_neo_feed(start_date, end_date)

        assert response.status_code == 400

    def test_neo_feed_no_api_key(self, monkeypatch):
        monkeypatch.setattr('config.settings.API_KEY', None)
        start_date = "2023-07-01"
        end_date = "2023-07-07"

        # Mock the response to return a 403 status code
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 403
            mock_get.return_value.json.return_value = {'error': 'API key missing'}

            response = get_neo_feed(start_date, end_date)
            assert response.status_code == 403
            assert 'error' in response.json()