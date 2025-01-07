class Player:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Player Name: {self.name}")

players = []
num_players = int(input("Enter the number of players: "))

for i in range(num_players):
    name = input("Enter player name: ")
    players.append(Player(name))
for player in players:
    player.display()