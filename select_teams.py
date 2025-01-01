
def print_teams():
    teams = {
            "Nets": ["Dennis Schroder", "Cam Thomas", "Ben Simmons", "Dorian Finney-Smith", "Nic Claxton"],
            "Mavericks": ["Luka Doncic", "Kyrie Irving", "Klay Thompson", "PJ Washington", "Dereck Lively II"],
            "Warriors": ["Stephen Curry", "Brandin Podziemski", "Andrew Wiggins", "Draymond Green", "Trayce Jackson-Davis"],
            "Lakers": ["Austin Reaves", "Dalton Knecht", "Rui Hachimura", "LeBron James", "Anthony Davis"],
            "Knicks": ["Jalen Brunson", "Mikal Bridges", "Josh Hart", "OG Anunoby", "Karl Anthony-Towns"],
            "Magic": ["Jalen Suggs", "Kentavious Caldwell-Pope", "Franz Wagner", "Paolo Banchero", "Goga Bitadze"]
        }

    team = input("Choose a team between the Nets, Mavericks, Warriors, Lakers, Knicks, and Magic: ").strip().capitalize()

    if team in teams:
            return f"{team} players: {', '.join(teams[team])}"
           
            player_name = input(f"Select a player from the {team}: ").strip().capitalize()

            if player_name.lower() in [player.lower() for player in teams[team]]:
                    return f"You selected {player_name} from the {team}."
            else:
                return f"{player_name} is not a valid player from the {team}."
    else:
            return f"Team not found in the data."
        

print(print_teams())