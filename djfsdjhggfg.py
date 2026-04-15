import requests

def clash(card):
    response = requests.get(f"https://github.com/martincarrera/clash-royale-api.git")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    print (data)
clash("D")
