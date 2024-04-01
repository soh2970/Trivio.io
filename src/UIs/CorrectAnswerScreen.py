import pygame
import sys
import os
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons

class CorrectAnswerScreen(ScreenBase):
    """
    Displays a congratulatory screen in a Pygame application when the player selects the correct
    answer to a question. This screen showcases a success message, indicates the positive impact
    of the player's correct answer on the game's boss (e.g., HP reduction), and prompts the player
    to proceed with the game.

    Inherits ScreenBase for Pygame window/screen setup and utilizes attributes and methods from
    ScreenBase to render elements specific to this success state.

    Attributes:
        level (int): Current game level or difficulty, affecting the damage to the boss on a correct answer.
        image (pygame.Surface): Success indication image displayed on this screen.
        header (str): Primary message to the player, acknowledging the correct answer.
        footer (str): Additional message informing about the impact on the boss's HP.
        continueButton (GameScreenButtons): Button widget to advance to the next question or game state.
        nextQuestion (bool): Flag to track if the player decides to move on to the next question.

    Methods:
        __init__(self, level):
            Initializes the CorrectAnswerScreen with the specified level of difficulty, loads the success
            image, sets up the screen's text messages based on the level, and prepares the "Continue"
            button.

        choiceMade(self):
            Marks the player's decision to proceed, setting the nextQuestion flag to True.

        draw(self):
            Draws the screen elements, including the success image, header, footer messages, and the
            "Continue" button, using Pygame's drawing methods. Inherits the basic screen drawing from
            ScreenBase and adds specific elements for this screen.

        handle_events(self):
            Handles Pygame events, such as button clicks and window resizing. Ensures that the screen
            responds appropriately to user inputs, including proceeding to the next question when the
            "Continue" button is clicked.
    """
    def __init__(self, level):
        super().__init__(self.MIN_WIDTH, self.MIN_HEIGHT)
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
        self.type = 'correctAnswerScreen'

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


