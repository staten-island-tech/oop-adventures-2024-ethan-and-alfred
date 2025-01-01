import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
TEAM_COLOR = (66, 74, 193)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Team and Player Selection")
font = pygame.font.SysFont("Arial", 20)
input_font = pygame.font.SysFont("Arial", 16)

def get_teams():
    return {
        "Nets": ["Dennis Schroder", "Cam Thomas", "Ben Simmons", "Dorian Finney-Smith", "Nic Claxton"],
        "Mavericks": ["Luka Doncic", "Kyrie Irving", "Klay Thompson", "PJ Washington", "Dereck Lively II"],
        "Warriors": ["Stephen Curry", "Brandin Podziemski", "Andrew Wiggins", "Draymond Green", "Trayce Jackson-Davis"],
        "Lakers": ["Austin Reaves", "Dalton Knecht", "Rui Hachimura", "LeBron James", "Anthony Davis"],
        "Knicks": ["Jalen Brunson", "Mikal Bridges", "Josh Hart", "OG Anunoby", "Karl Anthony-Towns"],
        "Magic": ["Jalen Suggs", "Kentavious Caldwell-Pope", "Franz Wagner", "Paolo Banchero", "Goga Bitadze"]
    }

def draw_text(text, font, color, position):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, position)

def main():
    teams = get_teams()
    selected_team = None
    selected_player = None
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(TEAM_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if not selected_team:
                    for i, team in enumerate(teams.keys()):
                        if 50 + i * 100 <= y <= 150 + i * 100:
                            selected_team = team

                elif selected_team and not selected_player:
                    team_members = teams[selected_team]
                    for i, member in enumerate(team_members):
                        if 200 + i * 20 <= y <= 220 + i * 20:
                            selected_player = member

        if not selected_team:
            draw_text("Choose a basketball team:", font, WHITE, (100, 10))
            for i, team in enumerate(teams.keys()):
                draw_text(team, input_font, WHITE, (100, 50 + i * 100))
        elif selected_team and not selected_player:
            draw_text(f"Team: {selected_team}", font, WHITE, (100, 50))
            draw_text("Select a player:", font, WHITE, (100, 100))
            for i, member in enumerate(teams[selected_team]):
                draw_text(member, input_font, WHITE, (200, 200 + i * 20))
        elif selected_team and selected_player:
            draw_text(f"Team: {selected_team}", font, WHITE, (100, 50))
            draw_text(f"Player: {selected_player}", font, WHITE, (100, 150))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
