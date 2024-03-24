"""
Win Game Screen

"""
from screen import ScreenBase
import pygame

class WinGameScreen(ScreenBase):

    def __init__(self):
        super().__init__()

    def draw(self):
        super().draw()

    def handle_events(self):
        # call parent class event handling
        super().handle_events()

    def run(self):
        super().run()

#initialize instance and run
if __name__ == '__main__':
    game_screen1 = WinGameScreen()
    game_screen1.run()