import requests
from config.settings import API_KEY, BASE_URL
from config import settings

def get_neo_feed(start_date, end_date):
    endpoint = f"{BASE_URL}/feed"
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'api_key': API_KEY
    }
    response = requests.get(endpoint, params=params)
    return response

def get_neo_lookup(asteroid_id):
    endpoint = f"{settings.BASE_URL}/neo/{asteroid_id}"
    params = {
        'api_key': settings.API_KEY # The get_neo_lookup function now reads the API_KEY from the settings module every time it is called. This ensures that any changes made by monkeypatch are picked up.
    }
    response = requests.get(endpoint, params=params)
    return response