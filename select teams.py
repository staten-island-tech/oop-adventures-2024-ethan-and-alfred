import os
import json

with open("./teams.json", encoding="utf8") as file:
    teams_data = json.load(file)

search_name = input("What team do you want to be? Choose the Nets, Lakers, Mavericks, Magic, Knicks or Warriors:").strip().lower()

found_teams = []

for team in teams_data:
    team_name = team.get('name', '').lower()  
    if team_name == search_name:
        found_teams.append(team)

if found_teams:
    print(f"Found the following team:")
    for team in found_teams:
        print("This is your current team.")
else:
    print("No team found. Choose the Nets, Lakers, Mavericks, Magic, Knicks or Warriors")

search_players = input("Name a player from your team.")
found_players = []

for players in teams_data:
    players_name = players.get('name', '').lower()  
    if players_name == search_players:
        found_players.append(players)
if found_players:
    print(f"Found your player:")
    for player in found_players:
        print(['players'])
else:
    print("No player found. Select another player from your team.")

