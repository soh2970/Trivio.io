"""

Base Screen Class

defines all the functions and constants that each UI class will need to implement

"""
import pygame
import sys

pygame.init()

class ScreenBase:
    """
    Serves as the foundational class for creating and managing UI screens in a Pygame application. It establishes a common framework
    and set of functionalities that are essential for the creation, display, and interaction of various UI components across different screens. 
    This includes handling common events such as screen resizing and quitting, as well as establishing a uniform appearance through predefined
    color and font attributes.

    Attributes:
        MIN_WIDTH (int): The minimum width allowed for the game window.
        MIN_HEIGHT (int): The minimum height allowed for the game window.
        SCREEN_SIZE (tuple): The default size of the game window, defined by MIN_WIDTH and MIN_HEIGHT.
        WHITE, BLACK, BLUE, GREY, DARKGREY, GREEN, RED (tuple): Color constants used throughout the UI for consistency.
        MODE_FONT, BUTTON_FONT, SMALLER_FONT, MID_FONT, MODE_SELECT_FONT, PARAGRAPH_FONT, MEDIUM_FONT, HEADING_FONT, BASE_FONT, SELECT_FONT (pygame.font.Font): 
            Font attributes for different textual elements within the UI, providing a consistent look and feel.
        screen (pygame.Surface): The main surface for drawing UI elements, acting as the primary display area for the application.
        running (bool): A flag to control the main event loop of the screen, indicating whether the application is actively running.

    Methods:
        __init__(self, width, height):
            Initializes a new screen with the specified dimensions, setting up the main display window and application caption.

        resize_screen(self, event):
            Adjusts the screen's dimensions based on user input while enforcing minimum size constraints, ensuring the UI remains usable.

        handle_events(self):
            Processes basic Pygame events, including quitting the game and resizing the window, maintaining core application functionality.

        draw(self):
            Fills the screen with a solid background color. Meant to be overridden in subclasses to include screen-specific drawing logic.

        update(self):
            A placeholder for updating the game state. Subclasses should override this method to implement specific game logic.

        run(self):
            Contains the main loop for the screen, responsible for drawing the screen, updating game state, and processing events.
    
    ScreenBase abstracts common functionalities needed by various screens within the application, promoting code reuse and reducing redundancy.
    Subclasses should extend ScreenBase to inherit these base functionalities while implementing additional features specific to the screen's purpose.
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