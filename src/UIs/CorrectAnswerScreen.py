import pygame
import sys
import os
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons

class CorrectAnswerScreen(ScreenBase):
    """
    A screen displayed in a Pygame application to inform the player that they have
    selected the correct answer for a question. It shows a celebratory message and
    indicates the impact of the correct answer on the game's boss (HP reduction).

    Inherits from ScreenBase, utilizing its setup for a Pygame window/screen.

    Attributes:
        level (int): The current level of difficulty, which affects the amount of damage
                     dealt to the boss for a correct answer.
        image (pygame.Surface): The image displayed on this screen, typically indicating success.
        header (str): The main message displayed to the player, indicating a correct answer.
        footer (str): Additional information shown to the player, such as the effect on the boss's HP.
        continueButton (GameScreenButtons): A button that allows the player to proceed to the next question.
        nextQuestion (bool): Flag indicating whether the player has chosen to proceed to the next question.

    Methods:
        choiceMade(self):
            Sets the flag indicating the player's decision to proceed to the next question.

        draw(self):
            Renders the screen, including the success image, header, footer, and the continue button.

        handle_events(self):
            Handles events such as button clicks and window resizing.
    """
    def __init__(self, level):
        super().__init__()
        self.level = level
        # Correctly calculate the path to the image file
        base_dir = os.path.dirname(os.path.dirname(__file__))  # This should navigate up to the project root
        correct_base_dir = os.path.abspath(os.path.join(base_dir, ".."))  # Ensure we're at the project root
        image_path = os.path.join(correct_base_dir, 'images', 'correctAnswer.png')
        self.image = pygame.image.load(image_path)
        self.header = "You got it CORRECT!"
        if (level == 1): self.footer = "- 4 HP to BOSS"
        elif (level == 2): self.footer = "- 6 HP to BOSS"
        elif (level == 3): self.footer = "- 10 HP to BOSS"
        else: self.footer = "unknown level"

        self.continueButton = GameScreenButtons(self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 + 200, 130, 40, "Continue", lambda: self.choiceMade(), self.WHITE, self.BLACK)
        self.nextQuestion = False

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




