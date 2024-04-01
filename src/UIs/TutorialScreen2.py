"""
Scoring Tutorial Screen

"""
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons
import pygame
import os
import sys

images_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'images')

class ScoringTutorialScreenTwo(ScreenBase):
    """
    The second tutorial screen within a Pygame application series, designed to educate the player on how scoring works
    in the game. This screen displays images and texts that explain the scoring mechanics, including how points are
    awarded for correct answers and the impact of incorrect answers.

    Inherits from ScreenBase, utilizing the base class's functionality for screen rendering and event handling while
    presenting tutorial-specific content and navigation options.

    Attributes:
        type (str): Screen identifier, indicating this is the second tutorial screen focused on scoring.
        prevTut (bool): Flag to transition back to the previous tutorial screen.
        toGameMode (bool): Flag to indicate completion of the tutorial and transition to the game mode selection screen.
        gamescreen_imageResized (pygame.Surface): Resized image depicting the game screen layout.
        gametext_imageResized (pygame.Surface): Resized image containing text explaining the scoring system.

    Methods:
        __init__(self):
            Initializes the tutorial screen with default settings and scoring-specific content.

        draw(self):
            Renders tutorial content related to scoring, including instructional images and text, as well as navigation
            buttons for reviewing previous information or completing the tutorial.

        toPrevTutorial(self):
            Sets the `prevTut` flag, indicating the user's request to return to the previous tutorial screen.

        toGameSelectMode(self):
            Sets the `toGameMode` flag, indicating the user's decision to exit the tutorial and proceed to the game mode
            selection screen.

        handle_events(self):
            Processes input events, including button clicks for navigation within or exit from the tutorial series.

        run(self):
            Contains the main loop for the tutorial screen, handling events and updating the display.

    ScoringTutorialScreenTwo further educates players on the game mechanics, specifically focusing on how their actions
    within the game influence their score. It's part of a tutorial series, each screen of which progressively builds
    upon the player's understanding of the game.
    """
    def __init__(self):
        super().__init__(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.type = 'tutorialTwo'
        self.prevTut = False
        self.toGameMode = False


    def draw(self):
        super().draw()
        # get the current width and height of the screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()


        #images
        self.gamescreen_image_rect = self.gamescreen_imageResized.get_rect(center = (self.width/13*4, self.height/7*3))
        self.screen.blit(self.gamescreen_imageResized, self.gamescreen_image_rect)
        self.gametext_image_rect = self.gametext_imageResized.get_rect(center = (self.width/26*21, self.height/7*3))
        self.screen.blit(self.gametext_imageResized, self.gametext_image_rect)

        #text heading
        self.text1 = self.SMALLER_FONT.render('How to Score Tutorial', True, self.BLACK)
        self.textRect1 = self.text1.get_rect(center = (self.width//2, self.height/12))
        self.screen.blit(self.text1, self.textRect1)
            
        #buttons
        self.next_button = GameScreenButtons(self.width/25*19, self.height/25*16, 170,40, "Previous Tutorial", lambda: self.toPrevTutorial(), self.BLUE, self.BLACK)
        self.next_button.draw(self.screen)
        self.done_button = GameScreenButtons(self.width/25*19, self.height/25*18, 140,40, "Done Tutorial", lambda: self.toGameSelectMode(), self.GREEN, self.BLACK)
        self.done_button.draw(self.screen)

    def toPrevTutorial(self):
        self.prevTut = True

    def toGameSelectMode(self):
        self.toGameMode = True


    def handle_events(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.next_button.handle_event(event)
            self.done_button.handle_event(event)

    def run(self):
            super().run()


    #load the game screen image
    gamescreen_image_path = os.path.join(images_dir, 'Tutorial_Screen.png')
    gamescreen_image = pygame.image.load(gamescreen_image_path)
    gamescreen_imageResized = pygame.transform.scale(gamescreen_image, (563,400))

    #load the instructions image
    gametext_image_path = os.path.join(images_dir, 'tutorial_text_2.png')
    gametext_image = pygame.image.load(gametext_image_path)
    gametext_imageResized = pygame.transform.scale(gametext_image, (318,239))

#initialize instance and run
if __name__ == '__main__':
    game_screen1 = ScoringTutorialScreenTwo()
    game_screen1.run()