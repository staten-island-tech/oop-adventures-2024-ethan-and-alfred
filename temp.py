class Player:
    def __init__(self, name, team, rating):
        self.data = {  
            "name": name,
            "team": team,
            "rating": rating
        }

    def display(self):
        print(f"Name: {self.data['name']}")
        print(f"Age: {self.data['team']}")
        print(f"Rating: {self.data['rating']}")

Player = Player("Lebron", "Lakers", "100")
Player.display()
