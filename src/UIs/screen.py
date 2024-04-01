"""

Base Screen Class

defines all the functions and constants that each UI class will need to implement

"""
import pygame
import sys

pygame.init()

class ScreenBase:
    """
    A base class for creating UI screens in a Pygame application. It provides a common
    structure and functionality for various screens, including screen resizing, event handling,
    and drawing base elements.

    Attributes and Constants:
        MIN_WIDTH (int): Minimum width for the Pygame window.
        MIN_HEIGHT (int): Minimum height for the Pygame window.
        SCREEN_SIZE (tuple): Default screen size (width, height).
        WHITE, BLACK, BLUE, GREY, DARKGREY, GREEN, RED (tuple): Color definitions.
        MODE_FONT, BUTTON_FONT, SMALLER_FONT, MID_FONT, MODE_SELECT_FONT, PARAGRAPH_FONT, MEDIUM_FONT, HEADING_FONT, BASE_FONT, SELECT_FONT (pygame.font.Font): Font definitions for text rendering.
        screen (pygame.Surface): The main Pygame window surface.
        running (bool): Flag indicating if the screen's main loop is running.

    Methods:
        __init__(self):
            Initializes the screen with default settings and starts the main loop.

        resize_screen(self, event):
            Resizes the screen based on user input while maintaining minimum dimensions.

        handle_events(self):
            Handles base Pygame events such as quitting the application or resizing the window.

        draw(self):
            Draws base elements onto the screen. Override this method in subclasses to draw specific UI elements.

        update(self):
            Updates the game state. Override this method in subclasses for specific screen updates.

        run(self):
            Contains the main loop for the screen, updating the display and handling events.
    """
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
    RED = (255,0,0)


    # fonts
    MODE_FONT = pygame.font.SysFont('Corbel',16) 
    BUTTON_FONT = pygame.font.SysFont('Corbel', 20)
    LEVEL_FONT = pygame.font.SysFont('Corbel', 28)
    HP_FONT = pygame.font.SysFont('Corbel', 30)
    SMALLER_FONT = pygame.font.SysFont('Corbel',32)
    MID_FONT = pygame.font.SysFont('Corbel', 42)
    MODE_SELECT_FONT = pygame.font.SysFont('Corbel',50)
    PARAGRAPH_FONT = pygame.font.SysFont('Corbel', 60)
    MEDIUM_FONT = pygame.font.SysFont('Corbel', 72)
    HEADING_FONT = pygame.font.SysFont('Corbel', 140)
    BASE_FONT = pygame.font.Font(None, 32)
    SELECT_FONT = pygame.font.SysFont(None, 50)

    # FUNCTIONS
    # initialize the game screen and caption
    def __init__(self, width, height):
        self.screen_width = int(width)
        self.screen_height = int(height)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption('Trivio')
        self.running = True
    # function to resize the screen 
    def resize_screen(self, event):
        # check if the new size is below the minimum size
        self.screen_width = max(event.w, self.MIN_WIDTH)
        self.screen_height = max(event.h, self.MIN_HEIGHT)

        # resize window if below minimum
        if self.screen_width<event.w or self.screen_height != event.h:
             window = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
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