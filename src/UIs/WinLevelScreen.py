import pygame

'''
from screen import ScreenBase
from GameScreenButtons import GameScreenButtons
'''
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons

import pygame
import os
import sys

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)



class WinLevelScreen(ScreenBase):
    """
    A screen displayed to the player upon successfully completing a level in the game. It congratulates
    the player on passing the level, and offers options to proceed to the next level, save the game, or
    access other options.

    Attributes:
        nextLvl (bool): Indicates whether the player has chosen to proceed to the next level.
        saveGame (bool): Indicates whether the player has chosen to save the current game state.
        type (str): Identifier for the screen type, set to 'winLevelScreen'.
        category (str): The category of questions the player was facing in the level.
        levelMove (int): Indicates the level progression, potentially used for determining the next level's difficulty or theme.

    Methods:
        draw(self):
            Renders the screen, displaying congratulatory messages, and drawing buttons for the player to choose their next action.
        
        continueGame(self):
            Sets the nextLvl flag to True, indicating the player's choice to continue to the next level.
        
        save(self):
            Sets the saveGame flag to True, indicating the player's choice to save their game state.
        
        handle_events(self):
            Processes input events, such as button clicks for proceeding to the next level, saving the game, or accessing options.
        
        run(self):
            Contains the main loop for the WinLevelScreen, handling events and updating the display.
    """

    def __init__(self):
        super().__init__(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.nextLvl = False
        self.saveGame = False
        self.type = 'winLevelScreen'
        self.catagory = ''
        self.levelMove = 0

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

    def continueGame(self):
        self.nextLvl = True
        print('button clicked')
    
    def save(self):
        self.saveGame = True

    def handle_events(self):
        # call parent class event handling
        super().handle_events()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                super().resize_screen(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.width/5*4 <= mouse[0] <= self.width/5*4+80 and self.height/15*13 <= mouse[1] <= self.height/15*13+90:
                    self.continueGame()
                if self.width/5*4 <= mouse[0] <= self.width/5*4+80 and self.height/15 <= mouse[1] <= self.height/15+30:
                    self.save()

    def run(self):
        super().run()

#initialize instance and run
if __name__ == '__main__':
    game_screen1 = WinLevelScreen()
    game_screen1.run()