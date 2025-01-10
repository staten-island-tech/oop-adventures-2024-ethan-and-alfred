class Players:
    def __init__(self, name, team, rating):
        self.name = name 
        self.team = team 
        self.rating = rating 

    def play(self):
        print({self.name}, {self.team})
    

player1 = Players("Lebron James", "Lakers", "100")
player2 = Players("Stephen Curry", "Warriors", "100")
player3 = Players("Kevin Durant", "Suns", "100")
player1.play()
player2.play()
player3.play()