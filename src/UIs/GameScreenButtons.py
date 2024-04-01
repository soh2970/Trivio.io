import pygame

class GameScreenButtons:
    """
    Represents a button in a Pygame application, capable of displaying text and executing a callback when clicked.

    This class is designed to create interactive buttons on a game screen. Each button can display custom text
    and perform an action defined by a callback function when the user clicks the button. The appearance of the button
    (color, text color, size) can be customized.

    Attributes:
        rect1 (pygame.Rect): The rectangle defining the position and size of the button's text area.
        rect2 (pygame.Rect): The rectangle defining the position and size of the button's border.
        text_color (tuple): The color of the button's text.
        colour (tuple): The background color of the button.
        text (str): The text displayed on the button.
        callback (function): The function to be called when the button is clicked.
        font (pygame.font.Font): The font used for the button's text.

    Methods:
        draw(self, screen):
            Renders the button on the provided Pygame screen, including its text and border.

        handle_event(self, event):
            Processes Pygame events, checking for mouse clicks on the button and triggering the callback if detected.
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
        text_surf = self.font.render(self.text, True, self.text_color)
        # Center the text on the button
        text_rect = text_surf.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        # Blit the text onto the screen
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse clicked
            if self.button.collidepoint(event.pos):  # Check if click is within button rect
                self.callback()  # Trigger the button's action/callback