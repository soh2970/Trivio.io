import sys
import os
import pygame


# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)

from GameScreenButtons import GameScreenButtons
from screen import ScreenBase
from HighScorer import HighScore


class InstructorDashboardScreen(ScreenBase):
    """
    
    """

    def __init__(self):
        super().__init__()
        self.userName = ''
        self.output = ''
        self.usernameValid = False
        self.scores = HighScore()
        self.active = False
        self.type = 'instructorDashboard'
        self.transitionToLogin = False

    def draw(self):
        super().draw()
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        userName_rect = pygame.Rect(330,190,200,32)

        titleOne = self.SMALLER_FONT.render('Enter Username', True, self.BLACK)
        titleTwo = self.SMALLER_FONT.render('For Player Details', True, self.BLACK)
        ok = self.SMALLER_FONT.render('OK', True, self.BLACK)
        cancel = self.SMALLER_FONT.render('Cancel', True, self.BLACK)
        esc = self.PARAGRAPH_FONT.render('x' , True , self.BLACK)

        pygame.draw.rect(self.screen, self.GREY, userName_rect)
        passwordSurface = self.BASE_FONT.render(self.userName, True, (0,0,0))
        self.screen.blit(passwordSurface, (userName_rect.x+5, userName_rect.y+5))

        pygame.draw.rect(self.screen,self.BLUE,[self.width/2+120,self.height/2-108,45,30]) 
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-405,self.height/2-293,30,30]) 
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-350,self.height/2-290,90,20]) 
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-170,self.height/2,350,300]) 


        self.screen.blit(titleOne, (self.width/2-100, self.height/2-200))
        self.screen.blit(titleTwo, ((self.width/2 - 100,self.height/2-150)))
        self.screen.blit(ok, (self.width/2+120, self.height/2-108))
        self.screen.blit(cancel, (self.width/2-349, self.height/2-285))
        self.screen.blit(esc , (self.width/2-400,self.height/2-300))

        if (self.usernameValid):
            i = 0

            for item in self.output.splitlines():
                outText = self.MODE_FONT.render(item, True, self.BLACK)
                out_rect = outText.get_rect(center=(self.width/2,self.height/2 + 100 + i * 20))
                self.screen.blit(outText , out_rect)
                i+= 1
        else:
            outText = self.MODE_FONT.render(self.output, True, self.BLACK)
            out_rect = outText.get_rect(center=(self.width/2,self.height/2 + 120))
            self.screen.blit(outText , out_rect)



    def check_username(self):
        if self.scores.checkForScore(self.userName):

            info = self.scores.getPlayerGameInfo(self.userName)
            self.output = ''
            for i in info.keys():
                self.output += str(i) + ': ' + str(info[i]) + '\n'
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