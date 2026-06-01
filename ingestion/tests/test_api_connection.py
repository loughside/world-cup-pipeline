
import requests
import os
from dotenv import load_dotenv

#============== Check API response ====================#

# Load environment variables from .env file
load_dotenv()

API_URL = 'https://v3.football.api-sports.io'
API_KEY = os.getenv("API_FOOTBALL_KEY")

# x-apisports-key is the required auth header for api-football.com
headers = {
    "x-apisports-key": API_KEY,
}

try:
    # Status endpoint confirms the key is valid and shows remaining daily quota
    response = requests.get(API_URL+'/odds/live?season=2022&league=1', headers=headers)

    # 'account' contains plan type, requests used today, and requests remaining
    result = response.json()
    print(result)

except Exception as e:
    print(f"Failed: {e}")