import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 844
SCREEN_HEIGHT = 600

# Base class for screens
class Screen:
    def __init__(self):
        self.next = self
    
    def process_events(self):
        pass
    
    def display(self, screen):
        pass
    
    def update(self, dt):
        pass
    
    def switch_to_screen(self, next_screen):
        self.next = next_screen
