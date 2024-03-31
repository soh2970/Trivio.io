"""
Win level screen
displays win and player stats
"""

from screen import ScreenBase
from GameScreenButtons import GameScreenButtons
import pygame

class WinLevelScreen(ScreenBase):
    """
    Class WinLevelScreen
    inherits all methods from ScreenBase
    """

    def __init__(self):
        super().__init__(self.MIN_WIDTH, self.MIN_HEIGHT)

    def draw(self):
        super().draw()
        # get the current width and height of the screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        
        #text
        self.text1 = self.HEADING_FONT.render('LEVEL', True, self.BLACK)
        self.textRect1 = self.text1.get_rect(center = (self.width//2, self.height/12*5))
        self.text2 = self.HEADING_FONT.render('PASSED', True, self.BLACK)
        self.textRect2 = self.text2.get_rect(center = (self.width//2, self.height/12*7))



        #line
        pygame.draw.line(self.screen, "Black", (self.width/3,self.height/12*8), (self.width/3*2, self.height/12*8), 1)

        # buttons
        self.level_button = pygame.draw.rect(self.screen, self.BLACK, (self.width/5*4, self.height/15*13, 80,30),1)
        self.next_level_text = self.BUTTON_FONT.render("Next Level", (self.level_button.centerx, self.level_button.centery), self.BLACK)
        self.next_level_rect = self.next_level_text.get_rect(center = self.level_button.center)

        self.save_button = pygame.draw.rect(self.screen, self.BLUE, (self.width/5*4, self.height/15*1, 80,30))
        self.save_border = pygame.draw.rect(self.screen, self.BLACK, (self.width/5*4, self.height/15*1, 80,30), 1)
        self.save_text = self.BUTTON_FONT.render("Save Game", (self.save_button.centerx, self.save_button.centery), self.BLACK)
        self.save_rect = self.save_text.get_rect(center = self.save_button.center)

        self.options_button = pygame.draw.rect(self.screen, self.BLUE, (self.width/5*4, self.height/15*2, 80,30))
        self.options_border = pygame.draw.rect(self.screen, self.BLACK, (self.width/5*4, self.height/15*2, 80,30), 1)
        self.options_text = self.BUTTON_FONT.render("Options", (self.options_button.centerx, self.options_button.centery), self.BLACK)
        self.options_rect = self.options_text.get_rect(center = self.options_button.center)

        # display text
        self.screen.blit(self.text1, self.textRect1)
        self.screen.blit(self.text2, self.textRect2)
        # display buttons
        self.screen.blit(self.next_level_text, self.next_level_rect)
        self.screen.blit(self.options_text, self.options_rect)
        self.screen.blit(self.save_text, self.save_rect)

    def handle_events(self):
        # call parent class event handling
        super().handle_events()

    def run(self):
        super().run()

#initialize instance and run
if __name__ == '__main__':
    game_screen1 = WinLevelScreen()
    game_screen1.run()