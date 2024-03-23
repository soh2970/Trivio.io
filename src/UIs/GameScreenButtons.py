import pygame

class GameScreenButtons:
    def __init__(self, x, y, width, height, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.color = (100, 200, 255)  # Button color
        self.text_color = (255, 255, 255)  # Text color
        self.font = pygame.font.Font(None, 32)  # Default font

    def draw(self, screen):
        # Draw the button rectangle
        pygame.draw.rect(screen, self.color, self.rect)
        # Render the text
        text_surf = self.font.render(self.text, True, self.text_color)
        # Center the text on the button
        text_rect = text_surf.get_rect(center=self.rect.center)
        # Blit the text onto the screen
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse clicked
            if self.rect.collidepoint(event.pos):  # Check if click is within button rect
                self.callback()  # Trigger the button's action/callback