import pygame

from src.constants import gui_constants


class Screen:
    def __init__(self, caption):
        self.screen_size = gui_constants.SCREEN_SIZE
        self.caption = caption
        self.running = False
        self.screen = None

    def __handle_default(self):
        pass

    def __get_event_handler(self, event):
        if event.type == pygame.QUIT:
            return self.__handle_quit_event
        return self.__handle_default

    def __handle_quit_event(self):
        self.running = False

    def __setup_screen(self):
        self.screen = pygame.display.set_mode(self.screen_size)

    def __event_loop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.__get_event_handler(event)()

    def start(self):
        self.__setup_screen()
        self.__event_loop()
