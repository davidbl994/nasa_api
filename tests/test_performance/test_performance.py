import time
from utils.helper import get_neo_feed, get_neo_lookup, get_apod

class TestPerformance:

    def test_neo_feed_response_time(self):
        start_time = time.time()
        response = get_neo_feed("2023-07-01", "2023-07-07")
        end_time = time.time()
        duration = end_time - start_time

        assert response.status_code == 200
        assert duration < 1.0, f"API response took too long: {duration}"

    def test_neo_lookup_resonse_time(self):
        start_time = time.time()
        response = get_neo_lookup(3542519)
        end_time = time.time()
        duration = end_time - start_time

        assert response.status_code == 200
        assert duration < 1.0, f"API response took too long: {duration}"