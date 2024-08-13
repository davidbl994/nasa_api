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
