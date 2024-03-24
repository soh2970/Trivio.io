import sys
import os
import pygame
from GameScreenButtons import GameScreenButtons
from screen import ScreenBase

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)


class DebuggerPasswordScreen(ScreenBase):
    def __init__(self):
        super().__init__()
        self.password_text = ''
        self.font = pygame.font.Font(None, 32)
        self.active = False
        self.input_box = pygame.Rect(self.SCREEN_SIZE[0] // 2 - 100, self.SCREEN_SIZE[1] // 2, 200, 32)
        self.input_box_color = pygame.Color('black')
        # OK button - Radio Style
        self.ok_button = GameScreenButtons(self.SCREEN_SIZE[0] // 2 + 55, self.SCREEN_SIZE[1] // 2 + 35, 40, 40, 'OK', self.check_password)
        # Cancel button - Rectangular Style
        self.cancel_button = GameScreenButtons(10, 10, 80, 30, 'Cancel', self.cancel)
        # We will draw the OK button differently to represent it as a radio button

    def check_password(self):
        if self.password_text == 'debug':
            print("Password correct, entering debugger mode...")
        else:
            print("Debugger credential invalid.")

    def cancel(self):
        print("Cancelled")
        self.running = False

    def handle_events(self):
        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_box.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False
                self.ok_button.handle_event(event)
                self.cancel_button.handle_event(event)

            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.password_text = self.password_text[:-1]
                else:
                    self.password_text += event.unicode

    def draw(self):
        self.screen.fill(self.WHITE)
        # Draw the input box
        pygame.draw.rect(self.screen, self.input_box_color, self.input_box, 2 if self.active else 1)
        # Render and blit password text
        text_surface = self.font.render(self.password_text, True, self.BLACK)
        self.screen.blit(text_surface, (self.input_box.x + 5, self.input_box.y + 5))
        
        # Draw "Debugger Password" label
        label_surf = self.font.render('Debugger Password', True, self.BLACK)
        label_rect = label_surf.get_rect(center=(self.SCREEN_SIZE[0] // 2, self.SCREEN_SIZE[1] // 2 - 50))
        self.screen.blit(label_surf, label_rect)

        # Draw "OK" button with rounded corners
        ok_button_rect = pygame.Rect(self.ok_button.rect.x, self.ok_button.rect.y, 50, 25)
        pygame.draw.rect(self.screen, self.ok_button.color, ok_button_rect, border_radius=5)
        if self.ok_button.text:
            ok_text_surf = self.ok_button.font.render(self.ok_button.text, True, self.ok_button.text_color)
            ok_text_rect = ok_text_surf.get_rect(center=ok_button_rect.center)
            self.screen.blit(ok_text_surf, ok_text_rect)

        # Draw "Cancel" button as a regular button
        self.cancel_button.draw(self.screen)

        # Update display
        pygame.display.flip()


    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    DebuggerPasswordScreen().run()