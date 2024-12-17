import os
import json
with open("./los angeles lakers.json", encoding="utf8") as teams_file:
    teams = json.load(teams_file)
search_name = input("Enter the name of Player to search for: ").strip().lower()
found_player = []
for player in teams:
    if player['name'].lower() == search_name:
        found_player.append(player)
if found_player:
    print("Found Player:")
    for player in found_player:
        print(f"- {player['name']} (Type: {', '.join(player['stats'])})")
else:
    print("No matching Player found. Make sure spelling is correct.")