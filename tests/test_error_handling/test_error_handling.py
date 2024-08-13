import requests.exceptions

from utils.helper import get_neo_feed, get_neo_lookup, get_apod
from unittest import mock

class TestErrorHandling:
    @mock.patch('utils.helper.requests.get')
    def test_network_failure(self, mock_get):
        # Simulate a network failure
        mock_get.side_effect = requests.exceptions.ConnectionError

        try:
            response = get_neo_feed("2023-07-01", "2023-07-07")
            assert False, "Expected ConnectionError"
        except requests.exceptions.ConnectionError:
            pass