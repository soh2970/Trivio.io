import sys
import os
import pygame


# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)

from src.UIs.GameScreenButtons import GameScreenButtons
from src.UIs.screen import ScreenBase
from src.HighScorer import HighScore


class InstructorDashboardScreen(ScreenBase):
    """
    A specialized screen within a Pygame application designed for instructors to view player
    details and high scores. It prompts the instructor to enter a username, and upon submission,
    displays the corresponding player's game information and high score if available.

    Inherits from ScreenBase to utilize foundational screen management and rendering functionalities.

    Attributes:
        userName (str): Stores the username entered by the instructor for lookup.
        output (str): The formatted string containing the player's game information and high score to be displayed.
        usernameValid (bool): Indicates whether the entered username matches an existing player.
        scores (HighScore): An instance of the HighScore class used to access player scores and information.
        active (bool): Tracks if the input field is currently active for text entry.
        type (str): Identifier for the type of screen, used in screen management, set to 'instructorDashboard'.
        transitionToLogin (bool): Flag indicating a request to return to the login screen.

    Methods:
        draw(self):
            Renders the screen's UI elements, including the username input field, informational text, and any retrieved player data.

        check_username(self):
            Validates the entered username against stored player data and updates the screen's output with the relevant information.

        cancel(self):
            Handles the operation to exit the instructor dashboard and return to the login screen.

        handle_events(self):
            Manages user inputs, including text entry, button clicks, and window resizing, facilitating interaction with the screen's functionalities.

        run(self):
            Executes the main event loop for the screen, continuously updating the display and responding to user actions.
    """

    def __init__(self, width, height):
        super().__init__(width, height)
        self.userName = ''
        self.output = ''
        self.usernameValid = False
        self.scores = HighScore()
        self.active = False
        self.type = 'instructorDashboard'
        self.transitionToLogin = False
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

    def draw(self):
        super().draw()

        userName_rect = pygame.Rect(self.screen_width/2 - 100, self.screen_height/2 - 120,200,32)

        titleOne = self.SMALLER_FONT.render('Enter Username', True, self.BLACK)
        titleTwo = self.SMALLER_FONT.render('For Player Details', True, self.BLACK)
        ok = self.SMALLER_FONT.render('OK', True, self.BLACK)
        cancel = self.SMALLER_FONT.render('Cancel', True, self.BLACK)
        esc = self.PARAGRAPH_FONT.render('x' , True , self.BLACK)

        pygame.draw.rect(self.screen, self.GREY, userName_rect)
        passwordSurface = self.BASE_FONT.render(self.userName, True, (0,0,0))
        self.screen.blit(passwordSurface, (userName_rect.x+5, userName_rect.y+5))

        pygame.draw.rect(self.screen,self.BLUE,[self.screen_width/2+120,self.screen_height/2-108,45,30]) 

        #back button
        pygame.draw.rect(self.screen,self.GREY,[self.screen_width/2-405,self.screen_height/2-293,30,30]) 

        #scores button
        pygame.draw.rect(self.screen,self.GREY,[self.screen_width/2-350,self.screen_height/2-290,90,20]) 

        #display of
        pygame.draw.rect(self.screen,self.GREY,[self.screen_width/2-170,self.screen_height/2,350,300]) 


        self.screen.blit(titleOne, (self.screen_width/2.5, self.screen_height/2-200))
        self.screen.blit(titleTwo, ((self.screen_width/2 - 100,self.screen_height/2-150)))
        self.screen.blit(ok, (self.screen_width/2+120, self.screen_height/2-108))
        self.screen.blit(cancel, (self.screen_width/2-349, self.screen_height/2-285))
        self.screen.blit(esc , (self.screen_width/2-400,self.screen_height/2-300))

        if (self.usernameValid):
            i = 0

            for item in self.output.splitlines():
                outText = self.MODE_FONT.render(item, True, self.BLACK)
                out_rect = outText.get_rect(center=(self.screen_width/2,self.screen_height/2 + 100 + i * 20))
                self.screen.blit(outText , out_rect)
                i+= 1
        else:
            outText = self.MODE_FONT.render(self.output, True, self.BLACK)
            out_rect = outText.get_rect(center=(self.screen_width/2,self.screen_height/2 + 120))
            self.screen.blit(outText , out_rect)



    def check_username(self):
        if self.scores.checkForScore(self.userName):

            info = self.scores.getPlayerGameInfo(self.userName)
            self.output = ''
            for i in info.keys():
                self.output += str(i) + ': ' + str(info[i]) + '\n'
            self.output += 'Highscore' + ': ' + str(self.scores.json_data[self.userName]['highscore']) + '\n'

            self.usernameValid = True

        else:
            self.output = 'No player matches the entered username.'
            self.usernameValid = False

    def cancel(self):
        self.transitionToLogin = True


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
                if self.width/2+120 <= mouse[0] <= self.width/2+165 and self.height/2-108 <= mouse[1] <= self.height/2+45:
                    self.check_username()



                #pygame.draw.rect(self.screen,self.GREY,[self.width/2-350,self.height/2-290,90,20]) 
                if self.width/2-350 <= mouse[0] <= self.width/2-200 and self.height/2-290 <= mouse[1] <= self.height/2-263:
                    self.cancel()
                    
                if self.width/2-405 <= mouse[0] <= self.width/2-385 and self.height/2-293 <= mouse[1] <= self.height/2-263:
                    self.cancel()
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_BACKSPACE:
                    self.userName = self.userName[:-1]
                else:
                    self.userName += event.unicode


    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()

if __name__ == "__main__":
    InstructorDashboardScreen().run()