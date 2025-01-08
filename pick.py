
import os
import json
teams = json.load(json)
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

class Player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def display(self):
        print(f"Player Name: {self.name}, Rating: {self.rating}")

players = {
    "Lebron James": Player("Lebron James", "100"),
    "Stephen Curry": Player("Stephen Curry", "100"),
    "Kevin Durant": Player("Kevin Durant", "100"),
}

print("Available Players:")
for name in players:
    print(name)

pick1 = input("Player 1, Enter the name of the player you want to select: ")
pick2 = input("Player 2, Enter the name of the player you want to select: ")

if pick1 in players:
    selected_player = players[pick1]
    print("\nYou selected:")
    selected_player.display()
else:
    
class Player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def display(self):
        print(f"Player Name: {self.name}, Rating: {self.rating}")

players = {
    "Lebron James": Player("Lebron James", "100"),
    "Stephen Curry": Player("Stephen Curry", "100"),
    "Kevin Durant": Player("Kevin Durant", "100"),
}

print("Available Players:")
for name in players:
    print(name)

pick1 = input("Player 1, Enter the name of the player you want to select: ")
pick2 = input("Player 2, Enter the name of the player you want to select: ")

if pick1 in players:
    selected_player = players[pick1]
    print("\nYou selected:")
    selected_player.display()
else:

    print("Player not found!")

if pick2 in players:
    selected_player = players[pick2]
    print("\nYou selected:")
    selected_player.display()
else:

    print("Player not found!")

    print("Player not found!")

