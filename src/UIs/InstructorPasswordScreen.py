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
    Displays a password entry screen specifically for instructors to gain access to administrative features
    within a Pygame application. This secure screen ensures that only authorized users can enter the instructor
    dashboard, where they can manage game content, view detailed player analytics, or perform other administrative tasks.

    Inherits from ScreenBase, utilizing general screen setup and event handling capabilities, while
    implementing specific functionalities for secure password entry and validation.

    Attributes:
        password_text (str): Dynamically updates to reflect the password as it's being entered by the user.
        active (bool): Indicates the current state of the password field, true if it's selected for input.
        type (str): Identifies the screen within the application, set to 'instructorPassword'.
        width, height (int): Current dimensions of the screen, useful for dynamically positioning UI elements.
        transitionToDashboard (bool): Signals a successful password entry and the need to transition to the instructor dashboard.
        transitionToLogin (bool): Indicates a request to return to the login screen, typically triggered by a 'Cancel' action.
        cancel_button (GameScreenButtons): Provides users with the option to cancel the operation and go back to the previous screen.

    Methods:
        draw(self):
            Constructs and displays the password input field, accompanying labels, and control buttons on the screen.

        check_password(self):
            Compares the entered password against a predetermined value, facilitating access control.

        cancel(self):
            Handles user requests to exit the password screen and potentially the application, ensuring a smooth user experience.

        handle_events(self):
            Processes all input events related to the password screen, including text entry, button interactions, and screen resizing.

        run(self):
            Encapsulates the main event loop for the screen, continuously rendering updates and responding to user inputs.

    The InstructorPasswordScreen class plays a crucial role in maintaining the application's integrity and security by restricting
    access to sensitive administrative functionalities through a password protection mechanism.
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