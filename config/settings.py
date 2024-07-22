import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('NASA_API_KEY')
BASE_URL = "https://api.nasa.gov/neo/rest/v1"