class Player:
    def __init__(self, name, team, rating):
        self.name = name
        self.team = team
        self.rating = rating

    def display(self):
        print(f"Player Name: {self.name}, Team: {self.team}, Rating: {self.rating}")

players = []
num_players = int(input("Enter the number of players: "))

for _ in range(num_players):
    name = input("Enter player name: ")
    team = input("Enter player team: ")
    rating = input("Enter player rating:")
    players.append(Player(name, team, rating))

for player in players:
    player.display()
