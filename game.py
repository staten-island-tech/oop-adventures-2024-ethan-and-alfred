import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Team Selection")

font = pygame.font.SysFont("Arial", 20)
input_font = pygame.font.SysFont("Arial", 16)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEAM_COLOR = (66, 74, 193)

def get_teams():
    return {
        "Nets": ["Dennis Schroder", "Cam Thomas", "Ben Simmons", "Dorian Finney-Smith", "Nic Claxton"],
        "Mavericks": ["Luka Doncic", "Kyrie Irving", "Klay Thompson", "PJ Washington", "Dereck Lively II"],
        "Warriors": ["Stephen Curry", "Brandin Podziemski", "Andrew Wiggins", "Draymond Green", "Trayce Jackson-Davis"],
        "Lakers": ["Austin Reaves", "Dalton Knecht", "Rui Hachimura", "LeBron James", "Anthony Davis"],
        "Knicks": ["Jalen Brunson", "Mikal Bridges", "Josh Hart", "OG Anunoby", "Karl Anthony-Towns"],
        "Magic": ["Jalen Suggs", "Kentavious Caldwell-Pope", "Franz Wagner", "Paolo Banchero", "Goga Bitadze"]
        }

teams = get_teams()
selected_team = None

clock = pygame.time.Clock()

def draw_text(text, font, color, position):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, position)

running = True
while running:
    screen.fill(TEAM_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if 100 <= x <= 300:
                team_options = ["Nets", "Mavericks", "Warriors", "Lakers", "Knicks", "Magic"]
                for i, team in enumerate(team_options):
                    if 50 + i * 100 <= y <= 150 + i * 100:
                        selected_team = team

    draw_text("Choose a basketball team:", font, WHITE, (100, 10))

    team_options = ["Nets", "Mavericks", "Warriors", "Lakers", "Knicks", "Magic"]
    for i, team in enumerate(team_options):
        draw_text(team, input_font, WHITE, (100, 50 + i * 100))

    if selected_team:
        draw_text(f"Team: {selected_team}", font, WHITE, (300, 150))

        team_members = teams[selected_team]
        y_name = 200
        for member in team_members:
            draw_text(member, input_font, WHITE, (300, y_name))
            y_name += 20  

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()