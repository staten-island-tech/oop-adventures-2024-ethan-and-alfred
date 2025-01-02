
def get_teams():
    return {
        "Nets": ["Dennis Schroder", "Cam Thomas", "Ben Simmons", "Dorian Finney-Smith", "Nic Claxton"],
        "Mavericks": ["Luka Doncic", "Kyrie Irving", "Klay Thompson", "PJ Washington", "Dereck Lively II"],
        "Warriors": ["Stephen Curry", "Brandin Podziemski", "Andrew Wiggins", "Draymond Green", "Trayce Jackson-Davis"],
        "Lakers": ["Austin Reaves", "Dalton Knecht", "Rui Hachimura", "LeBron James", "Anthony Davis"],
        "Knicks": ["Jalen Brunson", "Mikal Bridges", "Josh Hart", "OG Anunoby", "Karl Anthony-Towns"],
        "Magic": ["Jalen Suggs", "Kentavious Caldwell-Pope", "Franz Wagner", "Paolo Banchero", "Goga Bitadze"]
    }

def get_team_message(team, teams):
    if team in teams:
        return f"{team} players: {', '.join(teams[team])}"
    else:
        return "Team not found."
