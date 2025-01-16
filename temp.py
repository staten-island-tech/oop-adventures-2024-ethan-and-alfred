class Player:
    def __init__(self, name, team, rating):
        self.name = name 
        self.team = team 
        self.rating = rating

    def __str__(self):
        return f"{self.name}: {self.team}, {self.rating}"

Players = [
    Player("LeBron James", "Lakers", "100"),
    Player("Stephen Curry", "Warriors", "100"),
    Player("Kevin Durant", "Suns", "100"),
    Player("Kyrie Irving", "Mavericks", "100"),
    Player("Luka Doncic", "Mavericks", "100"),
    Player("Giannis Antetokounpo", "Bucks", "100")
]

print("Choose a player from the list:")
for i, player in enumerate(Players, start=1):
    print(f"{player}")

