import pygame
import sys

pygame.init()

width = 800
height = 600

color = (66, 74, 193)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Basketball Royale')

clock = pygame.time.Clock()
fps = 60

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                running = False
        screen.fill(color)

        pygame.display.flip()

        clock.tick(fps)
    pygame.quit()
    sys.exit()
