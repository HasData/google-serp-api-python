import sys
import os

sys.path.append(os.path.abspath('../'))

from google_serp_api import GoogleSerpApi  # noqa: E402

api_key = os.getenv('HASDATA_API_KEY', 'INSERT_YOUR_API_KEY_HERE')

client = GoogleSerpApi(api_key)
try:
    query = {
        "q": "Coffee",
        "location": "Austin,Texas,United States",
        "domain": "google.com",
        "gl": "us"
    }
    response = client.getSearchResults(query)
    data = response.json()
    print(data)
except Exception as e:
    print(f"Error occurred: {e}")
