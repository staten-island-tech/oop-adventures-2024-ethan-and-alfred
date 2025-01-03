import pygame
import sys
import json
import os


# Initialize Pygame
pygame.init()


# Screen dimensions and colors
WIDTH, HEIGHT = 800, 600
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (66, 74, 193)
BALL_COLOR = (255, 165, 0)
BASKET_COLOR = (255, 0, 0)


# Fonts
font_large = pygame.font.SysFont("fixedsys", 50)
font_small = pygame.font.SysFont("fixedsys", 30)


# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basketball Game")


# Load data
with open("./stats.json", encoding="utf8") as stats_file:
    data = json.load(stats_file)


teams = {
    team_data["team"]: {
        "players": {player["name"]: player["stats"] for player in team_data["players"]},
        "logo": None
    }
    for team_data in data["teams"]
}


# Load team logos
for team_name in teams:
    logo_path = f"./logos/{team_name.replace(' ', '_')}.png"
    if os.path.exists(logo_path):
        teams[team_name]["logo"] = pygame.image.load(logo_path)


# Utility functions
def draw_text(text, font, color, position):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, position)


# Game functions
def main_menu():
    selected_team = None
    selected_player = None
    clock = pygame.time.Clock()


    while not selected_team or not selected_player:
        screen.fill(BACKGROUND_COLOR)


        draw_text("Basketball Game", font_large, TEXT_COLOR, (200, 50))
        draw_text("Select a team:", font_small, TEXT_COLOR, (100, 150))


        # Display teams
        for i, (team_name, team_data) in enumerate(teams.items()):
            y = 200 + i * 100
            if team_data["logo"]:
                screen.blit(pygame.transform.scale(team_data["logo"], (50, 50)), (50, y))
            draw_text(team_name, font_small, TEXT_COLOR, (120, y))


        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i, (team_name, _) in enumerate(teams.items()):
                    if 200 + i * 100 <= y <= 250 + i * 100:
                        selected_team = team_name


        # If team selected, show players
        if selected_team:
            screen.fill(BACKGROUND_COLOR)
            draw_text(f"Team: {selected_team}", font_large, TEXT_COLOR, (100, 50))
            draw_text("Select a player:", font_small, TEXT_COLOR, (100, 150))
            for i, player in enumerate(teams[selected_team]["players"]):
                draw_text(player, font_small, TEXT_COLOR, (100, 200 + i * 50))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    for i, player in enumerate(teams[selected_team]["players"]):
                        if 200 + i * 50 <= y <= 250 + i * 50:
                            selected_player = player


        pygame.display.flip()
        clock.tick(60)


    return selected_team, selected_player


def gameplay(team, player):
    clock = pygame.time.Clock()
    player_pos = [WIDTH // 2, HEIGHT // 2]
    ball_pos = player_pos[:]
    ball_velocity = [0, 0]
    power = 0
    score = 0
    shooting = False
    basket_rect = pygame.Rect(WIDTH - 100, HEIGHT // 2 - 50, 50, 100)


    while True:
        screen.fill(BACKGROUND_COLOR)


        # Draw court and basket
        pygame.draw.rect(screen, BASKET_COLOR, basket_rect)


        # Draw player
        pygame.draw.circle(screen, TEXT_COLOR, player_pos, 20)


        # Draw ball
        pygame.draw.circle(screen, BALL_COLOR, ball_pos, 10)


        # Display score
        draw_text(f"Score: {score}", font_small, TEXT_COLOR, (10, 10))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    power = 0
                    shooting = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE and shooting:
                    shooting = False
                    ball_velocity = [power // 10, -(power // 20)]
            elif event.type == pygame.KEYUP:
                power = 0


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos[0] -= 5
        if keys[pygame.K_RIGHT]:
            player_pos[0] += 5
        if keys[pygame.K_UP]:
            player_pos[1] -= 5
        if keys[pygame.K_DOWN]:
            player_pos[1] += 5


        # Ball movement
        if shooting:
            power += 1
        else:
            ball_pos[0] += ball_velocity[0]
            ball_pos[1] += ball_velocity[1]
            ball_velocity[1] += 1  # Gravity


        # Check for scoring
        if basket_rect.collidepoint(ball_pos):
            score += 2
            ball_pos = player_pos[:]
            ball_velocity = [0, 0]


        pygame.display.flip()
        clock.tick(60)


# Main loop
if __name__ == "__main__":
    team, player = main_menu()
    gameplay(team, player)







