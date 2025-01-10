import random

# Player class
class Player:
    def __init__(self, name, team, rating):
        self.name = name
        self.team = team
        self.rating = int(rating)  # Rating could influence special rules later
        self.score = 0

    def take_shot(self, shot_type):
        """Simulate a shot based on the type."""
        if shot_type == "3-point":
            success_chance = 30  # 30% success rate
            points = 3
        elif shot_type == "midrange":
            success_chance = 60  # 60% success rate
            points = 2
        elif shot_type == "dunk":
            success_chance = 100  # 100% success rate
            points = 1
        else:
            print("Invalid shot type!")
            return 0

        # Determine if the shot is successful
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

# Game class
class BasketballGame:
    def __init__(self):
        self.players = [
            Player("LeBron James", "Lakers", 97),
            Player("Stephen Curry", "Warriors", 96),
            Player("Giannis Antetokounmpo", "Bucks", 95),
            Player("Kevin Durant", "Suns", 94),
            Player("Joel Embiid", "76ers", 93),
            Player("Nikola Jokic", "Nuggets", 92),
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

        chosen_player = self.players.pop(choice)  # Remove the chosen player from the list
        print(f"User {user_number} selected: {chosen_player}")
        return chosen_player

    def simulate_round(self, quarter_number):
        """Simulate a single round."""
        print(f"\n--- Quarter {quarter_number} ---")

        # User 1's turn
        print(f"\n{self.user1_player.name} (User 1), it's your turn!")
        shot_type = self.get_shot_choice()
        self.user1_player.take_shot(shot_type)

        # User 2's turn
        print(f"\n{self.user2_player.name} (User 2), it's your turn!")
        shot_type = self.get_shot_choice()
        self.user2_player.take_shot(shot_type)

        # Display scores after the round
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
        print("--- Welcome to the Basketball Game ---")

        # Users choose players
        self.user1_player = self.choose_player(1)
        self.user2_player = self.choose_player(2)

        # Play 4 rounds
        for quarter_number in range(1, 5):
            self.simulate_round(quarter_number)

        # Declare the winner
        self.declare_winner()

# Main function to start the game
if __name__ == "__main__":
    game = BasketballGame()
    game.run()
