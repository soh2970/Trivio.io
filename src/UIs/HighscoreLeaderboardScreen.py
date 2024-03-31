import sys
import os
import pygame
from GameScreenButtons import GameScreenButtons
from screen import ScreenBase

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)

from HighScorer import HighScore


class LeaderboardScreen(ScreenBase):
    """a
    
    """

    def __init__(self):
        super().__init__(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.scores = HighScore()
        self.active = False
        self.type = 'highscoreLeaderboard'
        self.goToMain = False

    def draw(self):
        super().draw()
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()


        titleOne = self.SMALLER_FONT.render('High Score Leaderboard', True, self.BLACK)
    
        cancel = self.SMALLER_FONT.render('Cancel', True, self.BLACK)
        esc = self.PARAGRAPH_FONT.render('x' , True , self.BLACK)

        pygame.draw.rect(self.screen,self.GREY,[self.width/2-405,self.height/2-293,30,30]) 
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-350,self.height/2-290,90,20]) 

        self.screen.blit(titleOne, (self.width/2-140, self.height/2-200))
        self.screen.blit(cancel, (self.width/2-349, self.height/2-285))
        self.screen.blit(esc , (self.width/2-400,self.height/2-300))
        
        rankings = self.scores.scoreRankings()
        table_width = 500
        table_height = 200
        cell_width = table_width / 3
        cell_height = table_height / 11

        header = ['Rank', 'Username', 'Score']

        endRankings = False

        for i in range(11):
            for j in range(3):
                if (i > len(rankings)): endRankings = True

                rect = pygame.Rect(j * cell_width + self.width/2 -230, i * cell_height + self.height/2-50, cell_width, cell_height)
                pygame.draw.rect(self.screen, (0,0,0), rect, 1)
                if (i == 0):
                    table_surface = self.MODE_FONT.render(header[j], True, (0,0,0))
                    table_rect = table_surface.get_rect(center=rect.center)
                    self.screen.blit(table_surface, table_rect)
                else:  
                    if not endRankings:
                        name = rankings[i-1][0]
                        userScore = rankings[i-1][1]['currentSavedGame']['score']
                        rows = [str(i), str(name), str(userScore)]
                    else:
                        rows = [str(i), '----', '----']
                    table_surface = self.MODE_FONT.render(rows[j], True, (0,0,0))
                    table_rect = table_surface.get_rect(center=rect.center)
                    self.screen.blit(table_surface, table_rect)
   
    def cancel(self):
        self.goToMain = True


    def handle_events(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                super().resize_screen(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                if self.width/2-405 <= mouse[0] <= self.width/2-385 and self.height/2-293 <= mouse[1] <= self.height/2-263:
                    self.cancel()
           


    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()

if __name__ == "__main__":
    LeaderboardScreen().run()