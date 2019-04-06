import pygame

from src.constants import gui_constants
from src.core.environment import Environment


class MainController:
    def __init__(self):
        self.env = Environment()

    def handle(self):
        screen = pygame.display.set_mode(gui_constants.SCREEN_SIZE)
        pygame.display.init()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()

    def __start_menu(self):
        pass

    def __event_controllers(self):
        pass
