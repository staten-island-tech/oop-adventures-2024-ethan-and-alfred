import random


class Player:
    def __init__(self, name, team, rating):
        self.name = name
        self.team = team
        self.rating = int(rating)
        self.score = 0




    def take_shot(self, shot_type):
        """Simulate a shot based on the type."""
        if shot_type == "3-point":
            success_chance = 30
            points = 3
        elif shot_type == "midrange":
            success_chance = 60
            points = 2
        elif shot_type == "dunk":
            success_chance = 100
            points = 1
        else:
            print("Invalid shot type!")
            return 0


        chance = random.randint(1, 100)
        if chance <= success_chance:
            print(f"Shot made! {points} points scored.")
            self.score += points
            return points
        else:
            print("Shot missed!")
            return 0




    def __str__(self):
        """String representation of the player."""
        return f"{self.name} (Team: {self.team}, Rating: {self.rating}, Score: {self.score})"


class BasketballGame:
    def __init__(self):
        self.players = [
            Player("LeBron James", "Lakers", 99),
            Player("Stephen Curry", "Warriors", 98),
            Player("Giannis Antetokounmpo", "Bucks", 96),
            Player("Kevin Durant", "Suns", 96),
            Player("Nikola Jokic", "Nuggets", 96),
            Player("Joel Embiid", "76ers", 94),
            Player("Jayson Tatum", "Celtics", 94),
            Player("Scottie Barnes", "Raptors", 89),
            Player("Jalen Brunson", "Knicks", 94),
            Player("Ben Simmons", "Nets", 99),
            Player("Jordan Poole", "Wizards", 87),
            Player("Lamelo Ball", "Hornets", 90),
            Player("Trae Young", "Hawks", 90),
            Player("Paolo Banchero", "Magic", 92),
            Player("Bam Adebayo", "Heat", 87),
            Player("Tyrese Haliburton", "Pacers", 82),
            Player("Donovan Mitchell", "Cavaliers", 89),
            Player("Cade Cunningham", "Pistons", 85),
            Player("Zach LaVine", "Bulls", 87),
            Player("Anthony Edwards", "Timberwolves", 93),
            Player("Shai Gilgeous-Alexander", "Thunder", 96),
            Player("Lauri Markkanen", "Jazz", 83),
            Player("Deandre Ayton", "Blazers", 80),
            Player("Domantas Sabonis", "Kings", 90),
            Player("Kawhi Leonard", "Clippers", 93),
            Player("Victor Wembanyama", "Spurs", 96),
            Player("Luka Doncic", "Mavericks", 95),
            Player("Ja Morant", "Grizzlies", 92),
            Player("Zion Williamson", "Pelicans", 92),
            Player("Alperen Sengun", "Rockets", 89)
        ]
        self.user1_player = None
        self.user2_player = None




    def choose_player(self, user_number):
        """Allow a user to choose a player."""
        print(f"\nUser {user_number}, choose your player:")
        for i, player in enumerate(self.players):
            print(f"{i + 1}. {player}")
        choice = int(input("Enter the number of your choice: ")) - 1




        while choice < 0 or choice >= len(self.players):
            print("Invalid choice. Please choose again.")
            choice = int(input("Enter the number of your choice: ")) - 1




        chosen_player = self.players.pop(choice)
        print(f"User {user_number} selected: {chosen_player}")
        return chosen_player




    def simulate_round(self, quarter_number):
        """Simulate a single round."""
        print(f"\n--- Quarter {quarter_number} ---")


        print(f"\n{self.user1_player.name} (User 1), it's your turn!")
        shot_type = self.get_shot_choice()
        self.user1_player.take_shot(shot_type)


        print(f"\n{self.user2_player.name} (User 2), it's your turn!")
        shot_type = self.get_shot_choice()
        self.user2_player.take_shot(shot_type)


        self.display_scores()




    def get_shot_choice(self):
        """Prompt the user to choose a shot type."""
        print("\nChoose your shot:")
        print("1. 3-point shot (30% chance, 3 points)")
        print("2. Midrange shot (60% chance, 2 points)")
        print("3. Dunk/Layup (100% chance, 1 point)")
        choice = int(input("Enter the number of your choice: "))




        while choice not in [1, 2, 3]:
            print("Invalid choice. Please choose again.")
            choice = int(input("Enter the number of your choice: "))




        if choice == 1:
            return "3-point"
        elif choice == 2:
            return "midrange"
        else:
            return "dunk"




    def display_scores(self):
        """Display the scores of both players."""
        print("\nCurrent Scores:")
        print(f"User 1 ({self.user1_player.name}): {self.user1_player.score} points")
        print(f"User 2 ({self.user2_player.name}): {self.user2_player.score} points")




    def declare_winner(self):
        """Declare the winner based on scores."""
        print("\n--- Game Over ---")
        print(f"{self.user1_player.name} (User 1) scored: {self.user1_player.score}")
        print(f"{self.user2_player.name} (User 2) scored: {self.user2_player.score}")




        if self.user1_player.score > self.user2_player.score:
            print("User 1 wins!")
        elif self.user2_player.score > self.user1_player.score:
            print("User 2 wins!")
        else:
            print("It's a tie!")




    def run(self):
        """Run the game."""
        print("Basketball Royale")


        self.user1_player = self.choose_player(1)
        self.user2_player = self.choose_player(2)


        for quarter_number in range(1, 5):
            self.simulate_round(quarter_number)


        self.declare_winner()


if __name__ == "__main__":
    game = BasketballGame()
    game.run()


