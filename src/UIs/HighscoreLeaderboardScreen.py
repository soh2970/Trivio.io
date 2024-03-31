import sys
import os
import pygame
from GameScreenButtons import GameScreenButtons
from screen import ScreenBase
<<<<<<< HEAD

=======
from HighScorer import HighScore
>>>>>>> e4fc9273f95955b74f69fb2691e7eee21d479388

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)
from HighScorer import HighScore



class LeaderboardScreen(ScreenBase):
    """
    
    """

    def __init__(self):
        super().__init__()
        self.scores = HighScore()
        self.active = False
        self.type = 'highscoreLeaderboard'

    def draw(self):
        super().draw()
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        

        titleOne = self.SMALLER_FONT.render('Leaderboard', True, self.BLACK)
        cancel = self.SMALLER_FONT.render('Cancel', True, self.BLACK)
        esc = self.PARAGRAPH_FONT.render('x' , True , self.BLACK)

        pygame.draw.rect(self.screen,self.GREY,[self.width/2-405,self.height/2-293,30,30]) 
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-350,self.height/2-290,90,20]) 

        self.screen.blit(titleOne, (self.width/2-100, self.height/2-200))
        self.screen.blit(cancel, (self.width/2-349, self.height/2-285))
        self.screen.blit(esc , (self.width/2-400,self.height/2-300))

        # display leaderboard
        rankings = self.scores.scoreRankings()
        for i in range(10):
            if (i < len(rankings)):
                output = str(i+1)+': ' +str(rankings[i][0]) + '   ' + str(rankings[i][1]['currentSavedGame']['score'])
            else:
                output = str(i+1)+': ----------------'
            outText = self.MODE_FONT.render(output, True, self.BLACK)
            out_rect = outText.get_rect(center=(self.width/2,self.height/2 - 100 + i*20))
            self.screen.blit(outText , out_rect)
          





   
    def cancel(self):
        print("Cancelled")
        self.running = False


    def handle_events(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                super().resize_screen(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                if self.width/2-405 <= mouse[0] <= self.width/2-385 and self.height/2-293 <= mouse[1] <= self.height/2-263:
                    pygame.quit()
                    sys.exit()
           


    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()

if __name__ == "__main__":
    LeaderboardScreen().run()