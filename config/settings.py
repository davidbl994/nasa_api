import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('NASA_API_KEY')
NEO_BASE_URL = "https://api.nasa.gov/neo/rest/v1"
APOD_BASE_URL = "https://api.nasa.gov/planetary/apod"