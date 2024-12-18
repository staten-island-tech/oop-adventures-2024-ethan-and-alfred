teams = {Brooklyn_Nets = ["Dennis Schroder", "Cam Thomas", "Ben Simmons", "Dorian Finney-Smith", "Nic Claxton"],
Dallas_Mavericks = ["Luka Doncic", "Kyrie Irving", "Klay Thompson", "PJ Washington", "Dereck Lively II"],
Golden_State_Warriors = ["Stephen Curry", "Brandin Podziemski", "Andrew Wiggins", "Draymond Green", "Trayce Jackson-Davis"],
Los_Angeles_Lakers = ["Austin Reaves", "Dalton Knecht", "Rui Hachimura", "LeBron James", "Anthony Davis"],
New_York_Knicks = ["Jalen Brunson", "Mikal Bridges", "Josh Hart", "OG Anunoby", "Karl Anthony-Towns"],
Orlando_Magic = ["Jalen Suggs", "Kentavious Caldwell-Pope", "Franz Wagner", "Paolo Banchero", "Goga Bitadze"]}


team = input(f"Choose a team from {', '.join(teams_players.keys())}: ")
if team in teams_players:
    print(f"{team} players: {', '.join(teams_players[team])}")
else:
    print("Invalid team!")
