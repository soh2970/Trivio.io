import pygame

class GameScreenButtons:
    def __init__(self, x, y, width, height, text, callback, colour, text_color):
        self.rect1 = pygame.Rect(x, y, width, height) # text
        self.rect2 = pygame.Rect(x, y, width, height) # border
        self.text_color = text_color 
        self.colour = colour
        self.text = text
        self.callback = callback
        if (len(text) > 20):
            self.font = pygame.font.SysFont('Corbel', 20)
        else: self.font = pygame.font.SysFont('Corbel', 32)  # Default font

    def draw(self, screen):
        # Draw the button rectangle
        button = pygame.draw.rect(screen, self.colour, self.rect1)
        pygame.draw.rect(screen, (0,0,0), self.rect2, 1)
        # Render the text
        text_surf = self.font.render(self.text, (button.centerx, button.centery), self.text_color)
        # Center the text on the button
        text_rect = text_surf.get_rect(center=self.rect1.center)
        # Blit the text onto the screen
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse clicked
            if self.rect.collidepoint(event.pos):  # Check if click is within button rect
                self.callback()  # Trigger the button's action/callback