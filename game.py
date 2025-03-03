# Example file showing a basic pygame "game loop"
import pygame
from main import playboard, size

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
screen.fill("white")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    y = 100
    for line in playboard:
        x = 100
        for square in line:
            pygame.draw.circle(screen, "grey", (x,y), 120 / size)
            x += 600 / (size-1)
        y += 600 / (size-1)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()