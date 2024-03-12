import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (173, 216, 230) # A light blue color
GREY = (200, 200, 200)
SCREEN_WIDTH, SCREEN_HEIGHT = 837, 525
FONT_NAME = pygame.font.match_font('arial')

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Trivia Game')


# Base Screen Class
class Screen:
    def __init__(self, app):
        self.app = app

    def handle_event(self, event):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def render(self, surface):
        raise NotImplementedError

    def switch_to_screen(self, screen_type):
        self.app.current_screen = self.app.screens[screen_type]

# Start Screen Class
class StartScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.font_large = pygame.font.Font(FONT_NAME, 80)
        self.font_button = pygame.font.Font(FONT_NAME, 30)
        self.start_button = pygame.Rect(SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 + 50, 140, 50)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.collidepoint(event.pos):
                self.switch_to_screen('login')

    def render(self, surface):
        surface.fill(WHITE)
        text_surf, text_rect = ("Welcome to TRIVIO", self.font_large)
        text_rect.center = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 4))
        surface.blit(text_surf, text_rect)

        pygame.draw.rect(surface, BLUE, self.start_button)
        text_surf, text_rect = ("+START", self.font_button, WHITE)
        text_rect.center = self.start_button.center
        surface.blit(text_surf, text_rect)

# Login Screen Class
class LoginScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.font_large = pygame.font.Font(FONT_NAME, 50)
        self.font_normal = pygame.font.Font(FONT_NAME, 30)
        self.username_box = pygame.Rect(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3, 300, 40)
        self.password_box = pygame.Rect(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2, 300, 40)
        self.ok_button = pygame.Rect(SCREEN_WIDTH // 3 + 350, SCREEN_HEIGHT // 2, 100, 40)
        self.user_text = ''
        self.pass_text = ''

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.username_box.collidepoint(pygame.mouse.get_pos()):
                if event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                else:
                    self.user_text += event.unicode
            elif self.password_box.collidepoint(pygame.mouse.get_pos()):
                if event.key == pygame.K_BACKSPACE:
                    self.pass_text = self.pass_text[:-1]
                else:
                    self.pass_text += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.ok_button.collidepoint(event.pos):
                print('Login attempt with:', self.user_text, self.pass_text)  # Placeholder for authentication logic

    def render(self, surface):
        surface.fill(WHITE)
        text_surf, text_rect = text_objects("Log in to get STARTED", self.font_large)
        text_rect.center = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 5))
        surface.blit(text_surf, text_rect)

        pygame.draw.rect(surface, GREY, self.username_box)
        text_surf, text_rect = text_objects(self.user_text, self.font_normal)
        text_rect.topleft = self.username_box.topleft
        surface.blit(text_surf, text_rect)

        pygame.draw.rect(surface, GREY, self.password_box)
        text_surf, text_rect = text_objects(self.pass_text, self.font_normal)
        text_rect.topleft = self.password_box.topleft
        surface.blit(text_surf, text_rect)

        pygame.draw.rect(surface, BLACK, self.ok_button)
        text_surf, text_rect = text_objects("OK", self.ok_button, WHITE)
        text_rect.center = self.ok_button.center
        surface.blit(text_surf, text_rect)

# App Class
class TriviaApp:
    def __init__(self):
        self.screens = {
            'start': StartScreen(self),
            'login': LoginScreen(self)
        }
        self.current_screen = self.screens['start']

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.current_screen.handle_event(event)

            self.current_screen.render(screen)
            pygame.display.flip()

        pygame.quit()
        sys.exit()

# Create app instance and run
app = TriviaApp()
app.run()
