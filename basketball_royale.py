import pygame
import sys
import json

pygame.init()

WIDTH, HEIGHT = 800, 600
TEXT_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (66, 74, 193)
BUTTON_COLOR = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basketball Royale")

font_large = pygame.font.SysFont("fixedsys", 30)
font_small = pygame.font.SysFont("fixedsys", 25)

with open("./stats.json", encoding="utf8") as stats_file:
    data = json.load(stats_file)

teams = {team_data["team"]: {player_data["name"]: player_data["stats"]
                              for player_data in team_data["players"]} for team_data in data["teams"]}

def draw_text(text, font, color, position):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, position)

def draw_button(text, font, color, position, width, height):
    pygame.draw.rect(screen, color, (position[0], position[1], width, height))
    draw_text(text, font, TEXT_COLOR, (position[0] + 10, position[1] + 10))

def main():
    selected_team, selected_player = None, None
    in_game = False
    clock = pygame.time.Clock()

    game_started = False  

    while True:
        screen.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if not in_game and 350 <= x <= 450 and 500 <= y <= 550:
                    in_game = True
                elif not selected_team:
                    selected_team = select_team(y)
                elif not selected_player and selected_team:
                    selected_player = select_player(y, selected_team)
                elif selected_team and selected_player:
                    if 350 <= x <= 450 and 500 <= y <= 550:
                        game_started = True

        if not in_game:
            draw_text("Basketball Royale", font_large, TEXT_COLOR, (100, 10))
            draw_button("Play", font_small, BUTTON_COLOR, (350, 500), 100, 50)
        elif not selected_team:
            draw_text("Choose a team:", font_large, TEXT_COLOR, (100, 10))
            display_teams()
        elif not selected_player:
            draw_text(f"Team: {selected_team}", font_large, TEXT_COLOR, (100, 50))
            draw_text("Select a player:", font_large, TEXT_COLOR, (100, 100))
            display_players(selected_team)
        elif not game_started:
            show_player_stats(selected_team, selected_player)
            draw_button("Start Game", font_small, BUTTON_COLOR, (350, 500), 100, 50)
        else:
            draw_text(f"Game has started with {selected_player} from {selected_team}!", font_large, TEXT_COLOR, (100, 250))

        pygame.display.flip()
        clock.tick(60)

def select_team(y):
    """Select team based on mouse Y position."""
    for i, team in enumerate(teams):
        if 50 + i * 100 <= y <= 150 + i * 100:
            return team
    return None

def select_player(y, team):
    """Select player from the team based on mouse Y position."""
    for i, player in enumerate(teams[team]):
        if 200 + i * 20 <= y <= 220 + i * 20:
            return player
    return None

def display_teams():
    """Display the available teams."""
    for i, team in enumerate(teams):
        draw_text(team, font_small, TEXT_COLOR, (100, 50 + i * 100))

def display_players(team):
    """Display the players of the selected team."""
    for i, player in enumerate(teams[team]):
        draw_text(player, font_small, TEXT_COLOR, (200, 200 + i * 20))

def show_player_stats(team, player):
    """Display the selected player's stats."""
    stats = teams[team][player]
    draw_text(f"Team: {team}", font_large, TEXT_COLOR, (100, 50))
    draw_text(f"Player: {player}", font_large, TEXT_COLOR, (100, 150))
    draw_text(f"Height: {stats['height']}", font_small, TEXT_COLOR, (100, 200))
    draw_text(f"Athleticism: {stats['athleticism']}", font_small, TEXT_COLOR, (100, 220))
    draw_text(f"Shooting: {stats['shooting']}", font_small, TEXT_COLOR, (100, 240))
    draw_text(f"Defense: {stats['defense']}", font_small, TEXT_COLOR, (100, 260))
    draw_text(f"Playmaking: {stats['playmaking']}", font_small, TEXT_COLOR, (100, 280))
    draw_text(f"Rebounding: {stats['rebounding']}", font_small, TEXT_COLOR, (100, 300))

if __name__ == "__main__":
    main()