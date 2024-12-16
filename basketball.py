import json
with open("./teams.json", encoding="utf8") as teams_file:
    teams = json.load(teams_file)
search_name = input("Enter the name of teams to search for: ").strip().lower()
found_team = []
for teams in teams:
    if teams['name'].lower() == search_name:
        found_team.append(teams)
if found_team:
    print("Found teams:")
    for teams in found_team:
        print(f"- {teams['name']} (players: {teams['players']})")
else:
    print("No matching teams found. Make sure spelling is correct.")