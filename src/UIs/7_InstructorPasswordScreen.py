"""

    Instructor Password Screen
    
    A screen that prompts for a instructor password. It's a part of the game's security feature,
    which allows access to instructor functionalities after successful password authentication.

    Attributes:
        password_text (str): Text entered by the user in the password input field.
        font (pygame.font.Font): Font used for rendering text on the screen.
        active (bool): Status of the input field; 'True' if active, 'False' otherwise.
        input_box (pygame.Rect): The rectangular area for the password input field.
        input_box_color (pygame.Color): The color of the input box border.
        ok_button (GameScreenButtons): The button object for submitting the password.
        cancel_button (GameScreenButtons): The button object for cancelling and closing the screen.

    Methods:
        __init__: Initializes the InstructorPassword with the required attributes.
        check_password: Validates the entered password and prints the result to the console.
        cancel: Handles the cancel action and stops the screen's run loop.
        handle_events: Handles the input events for the input box and buttons.
        draw: Renders the input box, buttons, and labels onto the screen.
        run: Contains the main loop to keep the screen running and responsive to user actions.

    """


import sys
import os
import pygame
from GameScreenButtons import GameScreenButtons
from screen import ScreenBase

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)


class InstructorPassword(ScreenBase):

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
        """
        Checks if the entered password is correct, allowing access to instructor mode.
        Prints a message to the console indicating whether access is granted or denied.
        """
        #alterable
        if self.password_text == 'Instructor':
            print("Password correct, entering instructor mode...")
        else:
            print("Instructor credential invalid.")


    def cancel(self):
        """
        Cancels the instructor access attempt and exits the password screen.
        """
        print("Cancelled")
        self.running = False


    def handle_events(self):
        """
        Handles keyboard and mouse events for the password input and buttons. This includes
        typing in the input box, clicking the 'OK' or 'Cancel' buttons, and exiting the screen.
        """
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
        """
        Draws the UI elements onto the screen, including the input box, buttons, and label.
        This method updates the appearance of the input box and buttons based on user interaction.
        """
        self.screen.fill(self.WHITE)
        # Draw the input box
        pygame.draw.rect(self.screen, self.input_box_color, self.input_box, 2 if self.active else 1)
        # Render and blit password text
        text_surface = self.font.render(self.password_text, True, self.BLACK)
        self.screen.blit(text_surface, (self.input_box.x + 5, self.input_box.y + 5))
        
        # Draw "Debugger Password" label
        label_surf = self.font.render('Instructor Password', True, self.BLACK)
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
        """
        Runs the main event loop for the password screen, keeping it active and responsive.
        Continuously calls the 'handle_events' and 'draw' methods to process input and update the UI.
        """
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    InstructorPassword().run()