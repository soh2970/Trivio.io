import pygame

class WinLevelScreen:
    def __init__(self, screen, font, current_level, category, player, boss, score):
        self.screen = screen
        self.font = font
        self.current_level = current_level
        self.category = category
        self.player = player
        self.boss = boss
        self.score = score
        self.next_level = False  # This flag will be used to determine if the "Next Level" button was clicked
        
        # Assuming a resolution of 800x600 for simplicity
        self.screen_width = 800
        self.screen_height = 600
        self.button_color = (0, 255, 0)  # Green color
        self.text_color = (255, 255, 255)  # White color
        self.button_rect = pygame.Rect(self.screen_width // 2 - 100, self.screen_height // 2, 200, 50)
        self.button_text = "Next Level"
        
    def draw(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black background
        
        # Draw the "Next Level" button
        pygame.draw.rect(self.screen, self.button_color, self.button_rect)
        text_surf = self.font.render(self.button_text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.button_rect.center)
        self.screen.blit(text_surf, text_rect)

        # You can add more elements to display as needed, such as current score, level, etc.

    def check_click(self, position):
        if self.button_rect.collidepoint(position):
            self.next_level = True  # The "Next Level" button was clicked

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.check_click(event.pos)
