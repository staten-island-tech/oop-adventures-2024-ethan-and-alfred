import json
with open("./stats.json", encoding="utf8") as players_file:
    stats = json.load(players_file)
search_name = input("Enter the name of player to search for: ").strip().lower()
found_player = []
for player in stats:
    if player['name'].lower() == search_name:
        found_player.append(player)
if found_player:
    print("Found player:")
    for player in found_player:
        print(f"- {player['name']}{player['stats']}")
else:
    print("No matching player found. Make sure spelling is correct.")