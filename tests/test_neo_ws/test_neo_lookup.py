from utils.helper import get_neo_lookup
from config import settings
class TestNeoLookUp:
    def test_valid_asteroid_id(self):
        asteroid_id = 3542519,
        response = get_neo_lookup(asteroid_id)

        assert response.status_code == 200
        data = response.json()
        assert 'neo_reference_id' in data

    def test_invalid_asteroid_id(self):
        asteroid_id = 9999999,
        response = get_neo_lookup(asteroid_id)

        assert response.status_code == 404

    def test_invalid_api_key(self, monkeypatch):
        invalid_api_key = 'INVALID_API_KEY'
        monkeypatch.setattr(settings, 'API_KEY', invalid_api_key)

        asteroid_id = 3542519
        response = get_neo_lookup(asteroid_id)

        print("Using API Key:", settings.API_KEY)
        print("Status Code:", response.status_code)
        print("Response Content:", response.content)

        assert response.status_code in [403]  # Adjust based on actual API response
        data = response.json()
        assert 'error' in data or 'message' in data

    def test_missing_api_key(self, monkeypatch):
        monkeypatch.setattr(settings, 'API_KEY', None)

        asteroid_id = 3542519
        response = get_neo_lookup(asteroid_id)

        print("Response Content:", response.content)
        assert response.status_code in [403]
        data = response.json()
        assert 'error' in data or 'message' in data