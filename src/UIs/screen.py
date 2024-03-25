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
    GREY = (220,220,220)
    DARKGREY = (45,45,45)
    GREEN = (204, 245, 205)


    # fonts
    MODE_FONT = pygame.font.SysFont('Corbel',16) 
    BUTTON_FONT = pygame.font.SysFont('Corbel', 20)
    SMALLER_FONT = pygame.font.SysFont('Corbel',32)
    MODE_SELECT_FONT = pygame.font.SysFont('Corbel',50)
    PARAGRAPH_FONT = pygame.font.SysFont('Corbel', 60)
    MEDIUM_FONT = pygame.font.SysFont('Corbel', 72)
    HEADING_FONT = pygame.font.SysFont('Corbel', 140)
    BASE_FONT = pygame.font.Font(None, 32)
    SELECT_FONT = pygame.font.SysFont(None, 50)

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
    

