from utils.helper import get_apod
from config import settings

class TestAPOD:
    def test_valid_api_key_with_date(self):
        date = "2023-07-22"
        response = get_apod(date=date, start_date=None, end_date=None, count=None, thumbs=False)

        assert response.status_code == 200
        data = response.json()
        assert 'date' in data
        assert data['date'] == '2023-07-22'

    def test_invalid_api_key(self, monkeypatch):
        invalid_api_key = 'INVALID_API_KEY'
        monkeypatch.setattr(settings, 'API_KEY', invalid_api_key)

        response = get_apod(date="2023-07-22", start_date=None, end_date=None, count=None, thumbs=False)

        print("Status Code:", response.status_code)
        print("Response Content:", response.content)

        assert response.status_code == 200  # Expecting fallback to demo key
        data = response.json()
        assert 'error' not in data