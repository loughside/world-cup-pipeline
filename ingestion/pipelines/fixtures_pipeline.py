
from ingestion.clients.api_football_client import FootballDataClient
from ingestion.loaders.sql_loader import SqlLoader

def run_fixtures_pipeline():
  client = FootballDataClient()            
  result = client.get_fixtures(league=1, season=2022)       
  
  loader = SqlLoader()
  loader.load_fixtures(result['response'])

if __name__ == "__main__":
  run_fixtures_pipeline()