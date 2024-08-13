# NASA API Project

This project demonstrates the use of Python to interact with NASA APIs, showcasing skills in Python,
pytest, and the 'requests' library. The project is organized to demostrate best practices in project
structure, API interaction, and testing strategies, focusing on GET requests due to the nature of the NASA APIs.

## Project Overview

This project leverages the following NASA APIs:
- **Astronomy Picture of the Day (APOD)**: Retrieves imagery and associated data from NASA's APOD service.
- **Near Earth Object Web Service (NeoWs)**: Provides information on near-Earth objects, allowing users to search for asteroids
based on their closest approach to Earth, lookup specific asteroids by their NASA JPL small body ID, and browse the overall dataset.

### Key files

- **config/settings.py**: Manages configuration settings, including API keys and base URLs.
- **utils/helper.py**: Contains utility functions to interact with the NASA APIs, such as `get_neo_feed`, `get_neo_lookup`, and `get_apod`.
- **tests/**: Contains all test cases structured by category, including edge cases, error handling, performance, and specific API tests.

## Setting Up the Project

### Prerequisites
- Python 3.11+
- `pip` (Python package installer)

### Installation

1. Clone the repository:
```bash
   git clone <repository-url>
   cd nasa_api_project
```

2. Create a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install the required packages:
```bash
   pip install -r requirements.txt
```
4. Set up your .env file with yoyr NASA API key:
```env
   NASA_API_KEY=your_nasa_api_key
```


