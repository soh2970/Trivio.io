import pygame
import sys
import os
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons

class IncorrectAnswerScreen(ScreenBase):
    """
    A screen displayed in a Pygame application to inform the player that they have
    selected an incorrect answer for a question. It shows a message indicating the mistake and
    indicates the impact of the incorrect answer on the player's health points (HP reduction).

    Inherits from ScreenBase, utilizing its setup for a Pygame window/screen.

    Attributes:
        level (int): The current level of difficulty, which affects the amount of damage
                     dealt to the player for an incorrect answer.
        image (pygame.Surface): The image displayed on this screen, typically indicating failure.
        header (str): The main message displayed to the player, indicating an incorrect answer.
        footer (str): Additional information shown to the player, such as the effect on their HP.
        continueButton (GameScreenButtons): A button that allows the player to proceed to the next question.
        nextQuestion (bool): Flag indicating whether the player has chosen to proceed to the next question.

    Methods:
        choiceMade(self):
            Sets the flag indicating the player's decision to proceed to the next question.

        draw(self):
            Renders the screen, including the failure image, header, footer, and the continue button.

        handle_events(self):
            Handles events such as button clicks and window resizing.
    """
    def __init__(self, level):
        super().__init__(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.level = level
        # Correctly calculate the path to the image file
        base_dir = os.path.dirname(os.path.dirname(__file__))  # This should navigate up to the project root
        correct_base_dir = os.path.abspath(os.path.join(base_dir, ".."))  # Ensure we're at the project root
        image_path = os.path.join(correct_base_dir, 'images', 'wrongAnswer.png')
        self.image = pygame.image.load(image_path)
        self.header = "You got it INCORRECT"
        if (level == 1): self.footer = "- 4 HP to YOU"
        elif (level == 2): self.footer = "- 6 HP to YOU"
        elif (level == 3): self.footer = "- 10 HP to YOU"
        else: self.footer = "unknown level"

        self.continueButton = GameScreenButtons(self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 + 200, 130, 40, "Continue", lambda: self.choiceMade(), self.WHITE, self.BLACK)
        self.nextQuestion = False
        self.type = 'incorrectAnswerScreen'

    def choiceMade(self):
        self.nextQuestion = True

    def draw(self):
        super().draw()

        #draw image onto screen
        image_resized = pygame.transform.scale(self.image, (200,200))
        self.screen.blit(image_resized, (self.screen.get_width()/2 - 95, self.screen.get_height()/2 - 230))
        
        #draw header text onto screen
        text_surface = self.MEDIUM_FONT.render(self.header, True, self.BLACK)
        self.screen.blit(text_surface, (self.screen.get_width()/2 - 230, self.screen.get_height()/2 + 40))

        #draw footer text onto screen
        text_surface = self.SMALLER_FONT.render(self.footer, True, self.RED)
        self.screen.blit(text_surface, (self.screen.get_width()/2 - 65, self.screen.get_height()/2 + 130))

        #draw continue button
        self.continueButton.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            # user quits
            if event.type == pygame.QUIT: 
                self.running = False
                pygame.quit()
                sys.exit()
            # user resizing screen
            elif event.type == pygame.VIDEORESIZE:
                self.resize_screen(event)
                self.continueButton.rect = pygame.Rect(self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 + 200, 130, 40)
            
            self.continueButton.handle_event(event)