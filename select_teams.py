import json

teams = {
    "Nets": ["Dennis Schroder", "Cam Thomas", "Ben Simmons", "Dorian Finney-Smith", "Nic Claxton"],
    "Mavericks": ["Luka Doncic", "Kyrie Irving", "Klay Thompson", "PJ Washington", "Dereck Lively II"],
    "Warriors": ["Stephen Curry", "Brandin Podziemski", "Andrew Wiggins", "Draymond Green", "Trayce Jackson-Davis"],
    "Lakers": ["Austin Reaves", "Dalton Knecht", "Rui Hachimura", "LeBron James", "Anthony Davis"],
    "Knicks": ["Jalen Brunson", "Mikal Bridges", "Josh Hart", "OG Anunoby", "Karl Anthony-Towns"],
    "Magic": ["Jalen Suggs", "Kentavious Caldwell-Pope", "Franz Wagner", "Paolo Banchero", "Goga Bitadze"]
}

team = input("Choose a team. Choose the Nets, Mavericks, Warriors, Lakers, Knicks, or Magic: ").capitalize()

if team in teams:
    print(f"{team} players: {', '.join(teams[team])}")
    
    player = input("Choose a player from your selected team.").capitalize()

    with open("./stats.json", encoding="utf8") as stats:
        data = json.load(stats)

    if player in stats["stats"]:
        if "name" in json["stats"][player]: 
            print(f"Stats for {json['stats'][player]['name']}: {json['stats'][player]}")
    else:
        print(f"Stats for {player} are not available.")
else:
    print("This player is either not found or not on your team.")
