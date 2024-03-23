"""

Base Screen Class

defines all the functions and constants that each UI class will need to implement

"""
import pygame
import sys

pygame.init()

class ScreenBase:
    # CONSTANTS
    # base screen dimensions
    MIN_WIDTH = 844
    MIN_HEIGHT = 600
    SCREEN_SIZE = (MIN_WIDTH, MIN_HEIGHT)

    # colours
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    BLUE = (159,197,248)

    # fonts
    BUTTON_FONT = pygame.font.SysFont('Corbel', 20)
    PARAGRAPH_FONT = pygame.font.SysFont('Corbel', 60)
    HEADING_FONT = pygame.font.SysFont('Corbel', 140)

    # FUNCTIONS
    # initialize the game screen and caption
    def __init__(self):
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption('Trivio')
        self.running = True
    # function to resize the screen 
    def resize_screen(self, event):
        # check if the new size is below the minimum size
        new_width = max(event.w, self.MIN_WIDTH)
        new_height = max(event.h, self.MIN_HEIGHT)

        # resize window if below minimum
        if new_width<event.w or new_height != event.h:
             window = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
        else:
            # increase size
            window_size = (event.w, event.h)
            self.screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
    
    # handle base events like quitting or resizing screen
    def handle_events(self):
        for event in pygame.event.get():
            # user quits
            if event.type == pygame.QUIT: 
                self.running = False
                pygame.quit()
                sys.exit()
            # user resizing screen
            elif event.type == pygame.VIDEORESIZE:
                self.resize_screen(event)

    #add any specific screen elements here
    def draw(self):
        self.screen.fill(self.WHITE)
    
    #updating game state
    def update(self):
        pass
    
    #we need this
    def run(self):
        while self.running:
            self.draw()
            pygame.display.update()
            self.handle_events()
            self.update()
        pygame.quit()
    

