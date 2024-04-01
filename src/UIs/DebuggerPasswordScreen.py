import sys
import os
import pygame
from src.UIs.GameScreenButtons import GameScreenButtons
from src.UIs.screen import ScreenBase

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)
pygame.init()

class DebuggerPasswordScreen(ScreenBase):
    """
    Presents a secure entry point for accessing the debugger mode in a Pygame application by requiring
    a password. Users must input the correct password to proceed to the debugger dashboard. This security
    measure ensures that debugger access is restricted to authorized users only.

    Inherits from ScreenBase for common screen functionality while implementing specific features for
    password verification, input handling, and screen transition management.

    Attributes:
        password_text (str): Dynamically updated string representing the user's password input.
        active (bool): Flag indicating whether the password input field is actively being edited.
        type (str): Screen type identifier, set to 'debuggerPassword' for internal management purposes.
        width, height (int): Dimensions of the screen, updated dynamically for responsive layouts.
        transitionToDashboard (bool): True if password verification is successful and a transition to
            the debugger dashboard is requested.
        transitionToLogin (bool): True if the user opts to cancel and return to the login screen.
        cancel_button (GameScreenButtons): UI button to cancel the operation and return to the previous screen.

    Methods:
        draw(self): Renders the password input field, instructional text, and interactive buttons on the screen.
        check_password(self): Compares the user's input to the expected password and sets the transition flag
            appropriately based on the result.
        cancel(self): Handler for the cancel operation, setting the necessary flag to return to the login screen.
        handle_events(self): Manages user interactions, including text input, button presses, and screen resizing.
        run(self): Executes the main loop, updating screen content and responding to events in real time.
    """

    def __init__(self):
        super().__init__(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.password_text = ''
        self.active = False
        self.type = 'debuggerPassword'
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.transitionToDashboard = False
        self.transitionToLogin = False

        # Define button properties
        button_width = 100
        button_height = 40
        button_text_color = (0, 0, 0)
        button_bg_color = (255, 255, 255)

        #### test needed for Mac ####
        self.cancel_button = GameScreenButtons(self.width / 2 - 405, self.height / 2 - 293, button_width, button_height, 'Cancel', self.cancel, button_text_color, button_bg_color)

        

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

        self.screen.blit(titleOne, (self.width / 2 - 200, self.height / 2 - 200))
        self.screen.blit(titleTwo, (self.width / 2 - 50, self.height / 2 - 150))
        self.screen.blit(ok, (self.width / 2 + 105, self.height / 2 + 55))

    def check_password(self):
        if self.password_text == 'debug':
            print("Password correct, entering debugger mode...")
            self.transitionToDashboard = True  # Set the flag to True
        else:
            print("Debugger credential invalid.")

    def cancel(self):
        self.transitionToLogin = True


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
                if self.cancel_button.button.collidepoint(event.pos):
                    self.cancel_button.callback()


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