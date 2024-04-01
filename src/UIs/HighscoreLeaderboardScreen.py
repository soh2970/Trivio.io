import sys
import os
import pygame
from src.UIs.GameScreenButtons import GameScreenButtons
from src.UIs.screen import ScreenBase
from src.HighScorer import HighScore


# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)



class LeaderboardScreen(ScreenBase):
    """
    Displays a leaderboard screen in a Pygame application, listing the top scores achieved by players.
    This screen is responsible for fetching and displaying a ranked list of high scores from the game's
    database, allowing users to see where they stand among other players in terms of game performance.

    Inherits from ScreenBase to utilize core screen functionalities such as rendering and event handling,
    while incorporating specific features for displaying high score data.

    Attributes:
        scores (HighScore): An instance of the HighScore class, used to access and sort player high scores.
        active (bool): Indicates whether the leaderboard screen is currently active and responding to user input.
        type (str): Screen identifier, used within the application to manage different screens, set to 'highscoreLeaderboard'.
        goToMain (bool): Flag indicating whether there is a request to return to the main menu screen.

    Methods:
        draw(self):
            Renders the leaderboard, including the title, high score rankings, and a button to return to the main menu.

        toMain(self):
            Signals that the user has requested to return to the main menu screen.

        handle_events(self):
            Handles user inputs, specifically looking for interactions that indicate a desire to return to the main menu or close the application.

        run(self):
            Manages the main event loop for the leaderboard screen, continuously updating the display and responding to user actions.

    The LeaderboardScreen class enhances the game's competitiveness by providing a visible metric of success through high scores, encouraging players to improve their gameplay to climb the rankings.
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
    
        esc = self.BUTTON_FONT.render('Main Menu' , True , self.BLACK)

        pygame.draw.rect(self.screen,self.GREY,[self.width/2-405,self.height/2-293,90,20]) 
        #pygame.draw.rect(self.screen,self.GREY,[self.width/2-350,self.height/2-290,90,20]) 

        self.screen.blit(titleOne, (self.width/2-140, self.height/2-200))
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
                        userScore = rankings[i-1][1]['highscore']
                        rows = [str(i), str(name), str(userScore)]
                    else:
                        rows = [str(i), '----', '----']
                    table_surface = self.MODE_FONT.render(rows[j], True, (0,0,0))
                    table_rect = table_surface.get_rect(center=rect.center)
                    self.screen.blit(table_surface, table_rect)

    def toMain(self):
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
                    
                if self.width/2-405 <= mouse[0] <= self.width/2-305 and self.height/2-290 <= mouse[1] <= self.height/2-260:
                    self.toMain()




    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()

if __name__ == "__main__":
    LeaderboardScreen().run()