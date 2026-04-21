import requests

from balldontlie import BalldontlieAPI


# Example: Fetch NBA teams

url = "https://api.balldontlie.io/v1/teams"
headers = {"Authorization": "f9eb4f44-79b4-48c2-9e40-38d25c59b741"}
response = requests.get(url, headers=headers)
data = response.json()

datas=[
    {'id': 1, 'conference': 'East', 'division': 'Southeast', 'city': 'Atlanta', 'name': 'Hawks', 'full_name': 'Atlanta Hawks', 'abbreviation': 'ATL'}
    {'id': 2, 'conference': 'East', 'division': 'Atlantic', 'city': 'Boston', 'name': 'Celtics', 'full_name': 'Boston Celtics', 'abbreviation': 'BOS'}, 
    {'id': 3, 'conference': 'East', 'division': 'Atlantic', 'city': 'Brooklyn', 'name': 'Nets', 'full_name': 'Brooklyn Nets', 'abbreviation': 'BKN'},
    {'id': 4, 'conference': 'East', 'division': 'Southeast', 'city': 'Charlotte', 'name': 'Hornets', 'full_name': 'Charlotte Hornets', 'abbreviation': 'CHA'},
    {'id': 5, 'conference': 'East', 'division': 'Central', 'city': 'Chicago', 'name': 'Bulls', 'full_name': 'Chicago Bulls', 'abbreviation': 'CHI'},
    {'id': 6, 'conference': 'East', 'division': 'Central', 'city': 'Cleveland', 'name': 'Cavaliers', 'full_name': 'Cleveland Cavaliers', 'abbreviation': 'CLE'},
    {'id': 7, 'conference': 'West', 'division': 'Southwest', 'city': 'Dallas', 'name': 'Mavericks', 'full_name': 'Dallas Mavericks', 'abbreviation': 'DAL'},
    {'id': 8, 'conference': 'West', 'division': 'Northwest', 'city': 'Denver', 'name': 'Nuggets', 'full_name': 'Denver Nuggets', 'abbreviation': 'DEN'},
    {'id': 9, 'conference': 'East', 'division': 'Central', 'city': 'Detroit', 'name': 'Pistons', 'full_name': 'Detroit Pistons', 'abbreviation': 'DET'},
    {'id': 10, 'conference': 'West', 'division': 'Pacific', 'city': 'Golden State', 'name': 'Warriors', 'full_name': 'Golden State Warriors', 'abbreviation': 'GSW'},
    {'id': 11, 'conference': 'West', 'division': 'Southwest', 'city': 'Houston', 'name': 'Rockets', 'full_name': 'Houston Rockets', 'abbreviation': 'HOU'},
    {'id': 12, 'conference': 'East', 'division': 'Central', 'city': 'Indiana', 'name': 'Pacers', 'full_name': 'Indiana Pacers', 'abbreviation': 'IND'},
    {'id': 13, 'conference': 'West', 'division': 'Pacific', 'city': 'LA', 'name': 'Clippers', 'full_name': 'LA Clippers', 'abbreviation': 'LAC'},   
    {'id': 14, 'conference': 'West', 'division': 'Pacific', 'city': 'Los Angeles', 'name': 'Lakers', 'full_name': 'Los Angeles Lakers', 'abbreviation': 'LAL'},
    {'id': 15, 'conference': 'West', 'division': 'Southwest', 'city': 'Memphis', 'name': 'Grizzlies', 'full_name': 'Memphis Grizzlies', 'abbreviation': 'MEM'},
    {'id': 16, 'conference': 'East', 'division': 'Southeast', 'city': 'Miami', 'name': 'Heat', 'full_name': 'Miami Heat', 'abbreviation': 'MIA'},
    {'id': 17, 'conference': 'East', 'division': 'Central', 'city': 'Milwaukee', 'name': 'Bucks', 'full_name': 'Milwaukee Bucks', 'abbreviation': 'MIL'},


    ]
