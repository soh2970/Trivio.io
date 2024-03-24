"""
Instructor Password Screen

"""
from screen import ScreenBase
import pygame
<<<<<<< HEAD
import sys
import os

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)
# initializing the constructor 
pygame.init() 
=======

class InstructorPassScreen(ScreenBase):
>>>>>>> e098bfe87fe38a37d5ef00d8c3d2ffc00acc5fa8

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
    game_screen1 = InstructorPassScreen()
    game_screen1.run()