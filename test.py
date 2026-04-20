import requests

from balldontlie import BalldontlieAPI

# Initialize with your API key
api = BalldontlieAPI(api_key="783897db-dbe2-4176-8821-e9e0cf0820e1")

# Example: Fetch NBA teams
teams = api.nba.teams.list()
for team in teams:
    print(team[1])


