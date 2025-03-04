import pygame
from button import Button


class Window:
    def __init__(self, lines_number, playboard):
        pygame.init()
        self.resolution = (800,800)
        self.window = pygame.display.set_mode(self.resolution)
        self.window.fill("white")
        self.buttons = []
        self.lines_number = lines_number
        self.playboard = playboard
        self.space = 600 / (self.lines_number-1)
        self.create_buttons()
        self.create_circles()
        pygame.display.update()

    def create_buttons(self):
        for y, line in enumerate(self.playboard):
            for x, square in enumerate(line):
                if square.side_top:
                    self.buttons.append(Button(10, self.space - 40, 110 + x * self.space, 110 + y * self.space, self.window))
    
    def create_circles(self):
        y = 100
        for line in self.playboard:
            x = 100
            for square in line:
                pygame.draw.circle(self.window, "grey", (x,y), 20)
                x += self.space
            y += self.space


    def on_click(self, position):
        for button in self.buttons:
            result = button.on_click(position)
            if result:
                return result
