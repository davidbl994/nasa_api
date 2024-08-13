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

    @mock.patch('utils.helper.requests.get')
    def test_timeout(self, mock_get):
        # Simulate a request timeout
        mock_get.side_effect = requests.exceptions.Timeout

        try:
            response = get_neo_lookup(3542519)
            assert False, "Expected Timeout"
        except requests.exceptions.Timeout:
            pass