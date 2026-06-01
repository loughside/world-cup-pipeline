
import os
import requests
from dotenv import load_dotenv


class FootballDataClient:
    BASE_URL = 'https://v3.football.api-sports.io'

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("FOOTBALL_DATA_API_KEY")

    def get_fixtures(self, league, season):
        try:
          url = self.BASE_URL + f"/fixtures?league={league}&season={season}"
          headers = {"x-apisports-key": self.api_key}
          response = requests.get(url,headers=headers)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network Error: {e}")

        if response.status_code != 200:
          raise Exception(f"API error {response.status_code}")

        data = response.json()
        if data['errors']:
          raise Exception(f"API errors: {data['errors']}")
        
        return data