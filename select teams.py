import os 
import json
with open ("./teams.json", encoding="utf8") as teams:
    teams = json.load(teams)
search_name = input("What team do you want to be? Choose the Nets, Lakers, Mavericks, Magic, Knicks or Warriors:").strip().lower()
found_teams = []
for teams in teams:
    if teams == search_name:
        found_teams.append(teams)
if found_teams:
    print(['name'])
    for teams in found_teams:
        print(f'- is your current team.')
else:
    print("No team found. Choose the Nets, Lakers, Mavericks, Magic, Knicks or Warriors")