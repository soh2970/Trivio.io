import sys
import os
import pygame
from src.UIs.GameScreenButtons import GameScreenButtons
from src.UIs.screen import ScreenBase

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)
pygame.init()

class InstructorPasswordScreen(ScreenBase):
    """
    A screen for entering the instructor mode password in a Pygame application.

    This screen is responsible for accepting a password input from the user,
    validating it, and then either transitioning to the instructor dashboard
    screen upon successful password entry or remaining on the password screen
    if the entry is invalid. It also provides an option to cancel and return
    to the login screen.

    Attributes:
        password_text (str): The password input by the user.
        active (bool): Indicates whether the password input field is active.
        type (str): A string identifier for the screen type, set to 'instructorPassword'.
        width (int): The current width of the screen.
        height (int): The current height of the screen.
        transitionToDashboard (bool): Flag to indicate transition to the instructor dashboard screen.
        transitionToLogin (bool): Flag to indicate transition back to the login screen.
        cancel_button (GameScreenButtons): Button to cancel and trigger transition back to the login screen.

    Methods:
        draw(self):
            Renders the password input field, labels, and buttons on the screen.

        check_password(self):
            Validates the entered password against the expected value ('instructor').

        cancel(self):
            Sets the flag to transition back to the login screen.

        handle_events(self):
            Handles user input and system events such as input in the password field, button clicks,
            and screen resizing.

        run(self):
            Contains the main loop for the screen that handles events and renders the screen.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        self.password_text = ''
        self.active = False
        self.type = 'instructorPassword'
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

        titleOne = self.MEDIUM_FONT.render('Instructor', True, self.BLACK)
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
        if self.password_text == 'instruct':
            print("Password correct, entering instructor mode...")
            self.transitionToDashboard = True  # Set the flag to True
        else:
            print("Instructor credential invalid.")

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
    InstructorPasswordScreen().run()