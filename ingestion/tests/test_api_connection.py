
import requests
import os
from dotenv import load_dotenv

#============== Check API response ====================#

# Load environment variables from .env file
load_dotenv()

API_URL = 'https://v3.football.api-sports.io/status'
API_KEY = os.getenv("FOOTBALL_DATA_API_KEY")

# x-apisports-key is the required auth header for api-football.com
headers = {
    "x-apisports-key": API_KEY,
}

try:
    # Status endpoint confirms the key is valid and shows remaining daily quota
    response = requests.get(API_URL, headers=headers)

    # 'account' contains plan type, requests used today, and requests remaining
    result = response.json()['response']['account']
    print(result)

except Exception as e:
    print(f"Failed: {e}")