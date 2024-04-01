import pygame
import sys
import os
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons

class IncorrectAnswerScreen(ScreenBase):
    """
    Displays a notification screen within a Pygame application to inform the player of an incorrect answer attempt.
    This screen serves as feedback for the player, detailing the consequences of the incorrect answer, such as the
    reduction in the player's health points. It aims to enhance the learning experience by encouraging players to
    understand their mistakes and strive for improvement.

    Inherits from ScreenBase, leveraging shared functionalities for consistent screen management across the application.

    Attributes:
        level (int): Reflects the current difficulty level of the game, influencing the penalty for incorrect answers.
        image (pygame.Surface): Visual feedback indicating the incorrect answer, designed to engage the player's attention.
        header (str): Primary message to the player, acknowledging the incorrect selection.
        footer (str): Further details on the repercussions of the mistake, specifically the impact on the player's HP.
        continueButton (GameScreenButtons): Interactable element allowing the player to advance beyond the feedback screen.
        nextQuestion (bool): State indicator that transitions the game forward upon player interaction with the continue button.

    Methods:
        choiceMade(self):
            Captures the player's action to move forward, updating the `nextQuestion` flag to true.

        draw(self):
            Compiles and renders the screen elements, including the feedback image, textual information, and the continue button.

        handle_events(self):
            Manages input events, particularly focusing on interactions with the continue button and screen resizing requests.

    The IncorrectAnswerScreen class encapsulates the functionality required to provide immediate, informative feedback
    on player performance, contributing to an engaging and educational gameplay experience.
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
                self.continueButton.button = pygame.Rect(self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 + 200, 130, 40)
            
            self.continueButton.handle_event(event)