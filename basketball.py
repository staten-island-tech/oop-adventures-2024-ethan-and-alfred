class Players:
    def __init__(self, name, team, rating):
        self.name = name 
        self.team = team 
        self.rating = rating 

    def play(self):
        print(f"Hello, my name is {self.name}, I play for the {self.team}, and my rating is {self.rating}.")

player1 = Players("Lebron James", "Lakers", "100")
player2 = Players("Stephen Curry", "Warriors", "100")
player1.play()
player2.play()