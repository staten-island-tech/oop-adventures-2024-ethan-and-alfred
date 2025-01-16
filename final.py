import random

class Player:
    def __init__(self, name, team, rating):
        """Initialize the player with their name, team, rating, and score."""
        self.name = name
        self.team = team
        self.rating = int(rating)  # Ensure rating is an integer
        self.score = 0  # Starting score is 0

    def take_shot(self, shot_type):
        """Simulate a shot based on the shot type and update the player's score."""
        if shot_type == "3-point":
            success_chance = 30  # 30% chance of making a 3-point shot
            points = 3  # 3 points for a successful 3-point shot
        elif shot_type == "midrange":
            success_chance = 60  # 60% chance of making a midrange shot
            points = 2  # 2 points for a successful midrange shot
        elif shot_type == "dunk":
            success_chance = 70  # 70% chance of making a dunk
            points = 1  # 1 point for a successful dunk
        else:
            print("Invalid shot type!")  # Handle invalid shot type
            return 0

        # Simulate a shot by generating a random chance between 1 and 100
        chance = random.randint(1, 100)
        if chance <= success_chance:
            print(f"Shot made! {points} points scored.")
            self.score += points  # Add points to player's score
            return points
        else:
            print("Shot missed!")
            return 0  # No points if the shot is missed

    def __str__(self):
        """Return a string representation of the player."""
        return f"{self.name} (Team: {self.team}, Rating: {self.rating}, Score: {self.score})"

class BasketballGame:
    def __init__(self):
        """Initialize the game with a list of players."""
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
        self.user1_player = None  # Player chosen by user 1
        self.user2_player = None  # Player chosen by user 2

    def choose_player(self, user_number):
        """Allow a user to choose a player from the available list."""
        print(f"\nUser {user_number}, choose your player:")
        for i, player in enumerate(self.players):
            print(f"{i + 1}. {player}")  # Display all available players
        choice = int(input("Enter the number of your choice: ")) - 1  # Get player's choice

        # Ensure the choice is valid
        while choice < 0 or choice >= len(self.players):
            print("Invalid choice. Please choose again.")
            choice = int(input("Enter the number of your choice: ")) - 1

        # Remove chosen player from the list of available players
        chosen_player = self.players.pop(choice)
        print(f"User {user_number} selected: {chosen_player}")
        return chosen_player

    def simulate_round(self, quarter_number):
        """Simulate a round (quarter) of the game."""
        print(f"\n--- Quarter {quarter_number} ---")

        # User 1 takes their shot
        print(f"\n{self.user1_player.name} (User 1), it's your turn!")
        shot_type = self.get_shot_choice()  # Get shot type from user 1
        self.user1_player.take_shot(shot_type)

        # User 2 takes their shot
        print(f"\n{self.user2_player.name} (User 2), it's your turn!")
        shot_type = self.get_shot_choice()  # Get shot type from user 2
        self.user2_player.take_shot(shot_type)

        self.display_scores()  # Display the current scores after the round

    def get_shot_choice(self):
        """Prompt the user to choose a shot type (3-point, midrange, or dunk)."""
        print("\nChoose your shot:")
        print("1. 3-point shot (30% chance, 3 points)")
        print("2. Midrange shot (60% chance, 2 points)")
        print("3. Dunk/Layup (70% chance, 1 point)")
        choice = int(input("Enter the number of your choice: "))

        # Ensure the choice is valid
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
        """Display the current scores of both players."""
        print("\nCurrent Scores:")
        print(f"User 1 ({self.user1_player.name}): {self.user1_player.score} points")
        print(f"User 2 ({self.user2_player.name}): {self.user2_player.score} points")

    def declare_winner(self):
        """Declare the winner based on the final scores."""
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
        """Run the entire game, including player selection and rounds."""
        print("--- __________ ---")

        # Users select their players
        self.user1_player = self.choose_player(1)
        self.user2_player = self.choose_player(2)

        # Simulate the 4 quarters of the game
        for quarter_number in range(1, 5):
            self.simulate_round(quarter_number)

        # Declare the winner after all quarters
        self.declare_winner()

# Main program execution
if __name__ == "__main__":
    game = BasketballGame()  # Create an instance of the game
    game.run()  # Run the game