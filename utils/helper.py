import requests
from config.settings import API_KEY, NEO_BASE_URL, APOD_BASE_URL
from config import settings

def get_neo_feed(start_date, end_date):
    endpoint = f"{NEO_BASE_URL}/feed"
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'api_key': API_KEY
    }
    response = requests.get(endpoint, params=params)
    return response

def get_neo_lookup(asteroid_id):
    endpoint = f"{settings.NEO_BASE_URL}/neo/{asteroid_id}"
    params = {
        'api_key': settings.API_KEY # The get_neo_lookup function now reads the API_KEY from the settings module every time it is called. This ensures that any changes made by monkeypatch are picked up.
    }
    response = requests.get(endpoint, params=params)
    return response

def get_apod(date=None, start_date=None, end_date=None, count=None, thumbs=False):
    endpoint = f"{settings.APOD_BASE_URL}/"
    params = {
        'date': date,
        'start_date': start_date,
        'count': count,
        'thumbs': thumbs,
        'api_key': API_KEY
    }
    # Remove keys with None values
    params = {key: value for key, value in params.items() if value is not None}

    response = requests.get(endpoint, params=params)
    return response