from window import Window
import pygame
import sys
from game import SIZE, PLAYBOARD

window = Window(SIZE, PLAYBOARD)

def human_play():
    position = pygame.mouse.get_pos()
    result = window.on_click(position=position)
    if result:
        x, y = result
        
        return True
    return False





def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass


if __name__ == "__main__":
    main()
