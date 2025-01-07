<<<<<<< HEAD
import pygame
import json

# Load player data from JSON file
def load_players(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

class BasketballPlayer:
    def __init__(self, name, stats, color, x, y):
        self.name = name
        self.stats = stats  # Dictionary of stats
        self.color = color
        self.x = x
        self.y = y
        self.speed = 5  # Movement speed

    def move(self, keys):
        """Move the player based on arrow key inputs."""
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def draw(self, screen):
        """Draw the player on the screen."""
        pygame.draw.circle(screen, self.color, (self.x, self.y), 20)
        font = pygame.font.Font(None, 24)
        text = font.render(self.name.split()[0], True, (255, 255, 255))  # Display first name
        screen.blit(text, (self.x - 10, self.y - 10))

class BasketballGame:
    def __init__(self, players):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Basketball Game")
        self.clock = pygame.time.Clock()
        self.players = players
        self.selected_player = None

    def select_player(self):
        """Allow the user to select a player at the start of the game."""
        print("Select a player:")
        for i, player in enumerate(self.players):
            print(f"{i + 1}. {player.name}")
        choice = int(input("Enter the number of the player to control: ")) - 1
        self.selected_player = self.players[choice]

    def display_stats(self, player):
        """Display stats for the selected player in the console."""
        print(f"\n{player.name}'s Stats:")
        for stat, value in player.stats.items():
            print(f"{stat.capitalize()}: {value}")

    def run(self):
        """Run the main game loop."""
        running = True
        self.select_player()
        self.display_stats(self.selected_player)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if self.selected_player:
                self.selected_player.move(keys)

            self.screen.fill((0, 128, 0))  # Green background for the court
            for player in self.players:
                player.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    # Load player data from JSON file
    player_data = load_players("stats.json")

    # Initialize players
    players = []
    colors = [(255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]  # Colors for players
    for i, data in enumerate(player_data):
        player = BasketballPlayer(
            name=data["name"],
            stats=data["stats"],  # Include stats dictionary
            color=colors[i % len(colors)],
            x=100 + i * 100,  # Staggered initial positions
            y=300
        )
        players.append(player)

    # Start the game
    game = BasketballGame(players)
    game.run()
=======
class Player:
    def __init__(self, name, team, rating):
        self.name = name
        self.team = team
        self.rating = rating

    def display(self):
        print(f"Player Name: {self.name}, Team: {self.team}, Rating: {self.rating}")

<<<<<<< HEAD
Player = Player("Lebron", "Lakers", "100")
Player.display()
>>>>>>> a6da10d9408f29c7ddf3fd017131cbe02a63d8a8
=======
players = []
num_players = int(input("Enter the number of players: "))

for _ in range(num_players):
    name = input("Enter player name: ")
    team = input("Enter player team: ")
    rating = input("Enter player rating:")
    players.append(Player(name, team, rating))

for player in players:
    player.display()
>>>>>>> 0885c918f4ba7e671aece24c89db83838afa4019
