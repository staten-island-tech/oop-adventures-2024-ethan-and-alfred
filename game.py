import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
BASKET_WIDTH, BASKET_HEIGHT = 100, 10
BALL_RADIUS = 15
TEXT_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (66, 74, 193)
BASKET_COLOR = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Basketball Game")

# Fonts
font = pygame.font.SysFont("Arial", 30)

# Colors
WHITE = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill((0, 0, 255))  # Player color (blue)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()

        # Move left and right
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 165, 0), (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 60)
        self.falling = False
        self.y_velocity = 0
        self.x_velocity = 0

    def update(self):
        if self.falling:
            self.rect.x += self.x_velocity
            self.rect.y += self.y_velocity
            if self.rect.y > HEIGHT - 50:
                self.falling = False
                self.rect.center = (WIDTH // 2, HEIGHT - 60)

    def shoot(self, angle):
        self.falling = True
        self.y_velocity = -15
        self.x_velocity = angle

# Game variables
player = Player()
ball = Ball()
all_sprites = pygame.sprite.Group(player, ball)
baskets = pygame.Rect(WIDTH // 2 - BASKET_WIDTH // 2, 50, BASKET_WIDTH, BASKET_HEIGHT)
score = 0
game_over = False

# Main game loop
def game_loop():
    global score, game_over

    clock = pygame.time.Clock()

    while True:
        screen.fill(BACKGROUND_COLOR)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not ball.falling:
                    # Shoot the ball
                    ball.shoot(5)

        # Update game objects
        all_sprites.update()

        # Draw everything
        pygame.draw.rect(screen, BASKET_COLOR, baskets)

        # Ball collision with the basket
        if baskets.colliderect(ball.rect) and ball.falling:
            if HEIGHT - 60 > ball.rect.bottom > HEIGHT - 100:
                score += 1
                ball.falling = False
                ball.rect.center = (WIDTH // 2, HEIGHT - 60)

        # Display score
        score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
        screen.blit(score_text, (10, 10))

        # Draw player and ball
        all_sprites.draw(screen)

        # Game over condition (optional)
        if score >= 10:
            game_over = True
            game_over_text = font.render("Game Over! You win!", True, TEXT_COLOR)
            screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(60)

# Start game loop
game_loop()
