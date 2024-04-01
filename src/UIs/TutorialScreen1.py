"""
Tutorial Screen 1

"""
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons
import pygame
import os
import sys

images_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'images')

class GameTutorialScreenOne(ScreenBase):

    def __init__(self):
        super().__init__(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.type = 'tutorialOne'
        self.toNextPage = False
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
        self.text1 = self.SMALLER_FONT.render('How to Play Tutorial', True, self.BLACK)
        self.textRect1 = self.text1.get_rect(center = (self.width//2, self.height/12))
        self.screen.blit(self.text1, self.textRect1)
        
        #buttons
        self.next_button = GameScreenButtons(self.width/25*19, self.height/25*16, 140,40, "Next Tutorial", lambda: self.toNextTutorial(), self.BLUE, self.BLACK)
        self.next_button.draw(self.screen)
        self.done_button = GameScreenButtons(self.width/25*19, self.height/25*18, 140,40, "Done Tutorial", lambda: self.toGameModeSelect(), self.GREEN, self.BLACK)
        self.done_button.draw(self.screen)

    def toNextTutorial(self):
        self.toNextPage = True

    def toGameModeSelect(self):
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
    gametext_image_path = os.path.join(images_dir, 'tutorial_text_1.png')
    gametext_image = pygame.image.load(gametext_image_path)
    gametext_imageResized = pygame.transform.scale(gametext_image, (318,239))

#initialize instance and run
if __name__ == '__main__':
    game_screen1 = GameTutorialScreenOne()
    game_screen1.run()