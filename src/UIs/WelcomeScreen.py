import pygame 
import sys
import os

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)

from src.UIs.GameScreenButtons import GameScreenButtons
from src.UIs.screen import ScreenBase
import pygame

class WelcomeScreen(ScreenBase):
    """
    The initial screen displayed upon launching the game. It presents a welcoming message and
    a start button that transitions the user to the main game or login screen.

    Inherits from ScreenBase, utilizing its setup for a Pygame window/screen.

    Attributes:
        type (str): Identifier for the screen type, set to 'welcomeScreen'.
        buttons (list): A list containing the start button as a GameScreenButtons object.
        transitionToNextScreen (bool): Flag indicating whether the start button has been clicked, signaling a transition to the next screen.

    Methods:
        choiceMade(self):
            Sets the transitionToNextScreen flag to True, indicating the user's decision to proceed from the welcome screen.

        draw(self):
            Renders the welcome screen, including any welcoming messages and the start button.

        handle_events(self):
            Processes input events, specifically handling the start button click and potential window resizing.

        run(self):
            Contains the main loop for the WelcomeScreen, handling events and rendering updates.
    """

    def __init__(self):
        super().__init__()
        self.type = 'welcomeScreen'
        self.buttons = [
            GameScreenButtons(self.screen.get_width()/2-100,self.screen.get_height()/2+100,200,40, "start", lambda: self.choiceMade(), self.WHITE, self.BLACK)
        ]
        self.transitionToNextScreen = False

    def choiceMade(self):
        print("transitioning from mainmenu to log in screen")
        self.transitionToNextScreen = True

    def draw(self):
        super().draw()
        # get the current width and height of the screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.text = self.PARAGRAPH_FONT.render('START' , True , self.BLACK) 
        self.welcome = self.MEDIUM_FONT.render('WELCOME TO' , True , self.BLACK) 
        self.trivio = self.MEDIUM_FONT.render('T R I V I O' , True , self.BLACK) 

        """
        potentially delete
        """
        self.esc = self.PARAGRAPH_FONT.render('x' , True , self.BLACK) 
        
		#button
        for button in self.buttons:
            button.draw(self.screen)

        """
        potentially delete
        """
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-405,self.height/2-293,30,30]) 

		# superimposing the text onto our button 
        # self.screen.blit(self.text , (self.width/2-65,self.height/2+100))
        self.screen.blit(self.welcome, (self.width/2-200,self.height/2-100))
        self.screen.blit(self.trivio, (self.width/2,self.height/2))
        """
        potentially delete
        """
        self.screen.blit(self.esc , (self.width/2-400,self.height/2-300))

    def handle_events(self):
        # stores the (x,y) coordinates into the variable as a tuple
        self.mouse = pygame.mouse.get_pos() 

        for event in pygame.event.get():
            # user quits
            if event.type == pygame.QUIT: 
                self.running = False
                pygame.quit()
                sys.exit()
            # user resizing screen
            elif event.type == pygame.VIDEORESIZE:
                super().resize_screen(event)
                for button in self.buttons:
                    button.rect = pygame.Rect(self.screen.get_width()/2-100,self.screen.get_height()/2+100,200,40)

            for button in self.buttons:
                button.handle_event(event)
           
            """
            i dont think we need this on the welcome screen
            """
            # user clicking our exit button
            if event.type == pygame.MOUSEBUTTONDOWN: 
                #if the mouse is clicked on the x button the game is terminated 
                if self.width/2-405 <= self.mouse[0] <= self.width/2+435 and self.height/2-293 <=self.mouse[1] <= self.height/2-263:
                    pygame.quit()
                    sys.exit()
                          

    def run(self):
        super().run()

#initialize instance and run
if __name__ == '__main__':
    game_screen1 = WelcomeScreen()
    game_screen1.run()
