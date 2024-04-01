import pygame

class GameScreenButtons:
    """
    Provides an interactive button component for Pygame applications, designed to execute specific actions upon being clicked.
    This class enables the creation of visually customizable buttons that can display text and respond to user input, facilitating
    user interaction within the game. Each button can be individually configured to perform a distinct callback function, allowing
    for a wide range of interactive capabilities across various game screens.

    Attributes:
        x (int): The x-coordinate of the button's top-left corner.
        y (int): The y-coordinate of the button's top-left corner.
        width (int): The width of the button.
        height (int): The height of the button.
        text_color (tuple): The RGB color value for the text displayed on the button.
        colour (tuple): The RGB color value for the button's background.
        text (str): The label text displayed on the button.
        callback (function): A callback function that is executed when the button is clicked.
        font (pygame.font.Font): The font used for rendering the button's text. The font size adjusts based on the length of the text.

    Methods:
        draw(self, screen):
            Renders the button onto the specified Pygame screen object. This includes drawing the button's background, border, and text label.

        handle_event(self, event):
            Responds to Pygame events, specifically checking for mouse clicks within the button's boundaries. If a click is detected,
            the button's associated callback function is executed.

    The GameScreenButtons class streamlines the process of adding interactive elements to a game's UI, supporting enhanced player engagement
    through clear visual cues and responsive actions.
    """
    def __init__(self, x, y, width, height, text, callback, colour, text_color):
        '''
        self.rect1 = pygame.Rect(x, y, width, height) # text
        self.rect2 = pygame.Rect(x, y, width, height) # border
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_color = text_color 
        self.colour = colour
        self.text = text
        self.callback = callback
        if (len(text) > 20):
            self.font = pygame.font.SysFont('Corbel', 20)
        else: self.font = pygame.font.SysFont('Corbel', 28)  # Default font

    def draw(self, screen):
        # Draw the button rectangle
        self.button = pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        self.button_border = pygame.draw.rect(screen, (0,0,0), (self.x, self.y, self.width, self.height), 1)
        # Render the text
        text_surf = self.font.render(self.text, (self.button.centerx, self.button.centery), self.text_color)
        # Center the text on the button
        text_rect = text_surf.get_rect(center=self.button.center)
        # Blit the text onto the screen
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse clicked
            if self.button.collidepoint(event.pos):  # Check if click is within button rect
                self.callback()  # Trigger the button's action/callback