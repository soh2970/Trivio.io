import sys
import os
import pygame
from GameScreenButtons import GameScreenButtons
from screen import ScreenBase
from DebuggerDashboardScreen import DebuggerDashboardPage

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)


class DebuggerPasswordScreen(ScreenBase):
    """
    
    """

    def __init__(self):
        super().__init__()
        self.password_text = ''
        self.active = False
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        # Define button properties
        button_width = 100
        button_height = 40
        button_text_color = (0, 0, 0)
        button_bg_color = (255, 255, 255)

        #### test needed for Mac ####
        self.cancel_button = GameScreenButtons(self.width / 2 - 350, self.height / 2 - 290, button_width, button_height, 'Cancel', self.cancel, button_text_color, button_bg_color)
        self.exit_button = GameScreenButtons(self.width / 2 - 405, self.height / 2 - 293, button_width, button_height, 'x', self.exit, button_text_color, button_bg_color)

        

    def draw(self):
        super().draw()
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        password_rect = pygame.Rect(400, 300, 200, 32)

        titleOne = self.MEDIUM_FONT.render('Debugger', True, self.BLACK)
        titleTwo = self.MEDIUM_FONT.render('Password', True, self.BLACK)
        ok = self.SMALLER_FONT.render('OK', True, self.BLACK)

        pygame.draw.rect(self.screen, self.GREY, password_rect)
        passwordSurface = self.BASE_FONT.render(self.password_text, True, (0, 0, 0))
        self.screen.blit(passwordSurface, (password_rect.x + 5, password_rect.y + 5))

        pygame.draw.rect(self.screen, self.BLUE, [self.width / 2 + 100, self.height / 2 + 50, 45, 30])

        # Draw the buttons
        self.cancel_button.draw(self.screen)
        self.exit_button.draw(self.screen)

        self.screen.blit(titleOne, (self.width / 2 - 200, self.height / 2 - 200))
        self.screen.blit(titleTwo, (self.width / 2 - 50, self.height / 2 - 150))
        self.screen.blit(ok, (self.width / 2 + 105, self.height / 2 + 55))

    def check_password(self):
        if self.password_text == 'debug':
            print("Password correct, entering debugger mode...")
            dashboard_page = DebuggerDashboardPage(self.screen)  # Initialize the dashboard
            dashboard_page.run()
        else:
            print("Debugger credential invalid.")

    def cancel(self):
        print("Cancelled")
        self.running = False

    def exit(self):
        print("Exiting application...")
        pygame.quit()
        sys.exit()

    def handle_events(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                super().resize_screen(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.width / 2 + 100 <= mouse[0] <= self.width / 2 + 145 and self.height / 2 + 50 <= mouse[
                    1] <= self.height / 2 + 80:
                    self.check_password()

                # Check if buttons are clicked
                if self.cancel_button.rect1.collidepoint(event.pos):
                    self.cancel_button.callback()

                if self.exit_button.rect1.collidepoint(event.pos):
                    self.exit_button.callback()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.password_text = self.password_text[:-1]
                else:
                    self.password_text += event.unicode

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()


if __name__ == "__main__":
    DebuggerPasswordScreen().run()