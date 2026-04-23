import requests
import random
import tkinter
from balldontlie import BalldontlieAPI


# Example: Fetch NBA teams

url = "https://api.balldontlie.io/v1/teams"
headers = {"Authorization": "f9eb4f44-79b4-48c2-9e40-38d25c59b741"}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json() 
    print(data)
else:
    print(f"Error: {response.status_code}")

id = data["id"]
team = data['full_name'],['name']

print(id)
print(team)
