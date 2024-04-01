#saver
import pygame 
import sys
import os

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)

from src.UIs.GameScreenButtons import GameScreenButtons
from src.UIs.screen import ScreenBase
from src.UIs.OptionsScreen import OptionsScreen
import pygame

class WelcomeScreen(ScreenBase):
    """
    A welcoming interface for the game, presenting users with the initial screen upon launching the game.
    This screen displays a welcome message and provides a start button to transition the user to the main
    game interface or login screen, and an options button to customize game settings.

    Inherits from ScreenBase, leveraging its foundational setup for a consistent Pygame window/screen configuration.

    Attributes:
        type (str): Identifier for the screen type, set to 'welcomeScreen'.
        buttons (list): A list containing the start button, implemented as a GameScreenButtons object.
        transitionToNextScreen (bool): Flag indicating whether the start button has been clicked, signaling the user's intention to transition to the next screen.
        options (bool): Flag indicating whether the options button has been clicked, signaling the user's desire to view the options screen.
        audio_manager: Manages audio playback for the screen.
        optionsButton (GameScreenButtons): Button to open the options screen for adjusting settings such as volume.

    Methods:
        optionsChoice(self):
            Invokes the display of the options screen, allowing users to adjust game settings.

        choiceMade(self):
            Sets the transitionToNextScreen flag to True, indicating the user's decision to proceed from the welcome screen to the next phase of the game interface.

        draw(self):
            Renders the welcome screen, including welcoming messages, and the start and options buttons.

        handle_events(self):
            Processes input events, notably handling clicks on the start and options buttons and managing window resizing.

        run(self):
            Contains the main loop for the WelcomeScreen, facilitating event handling and screen updates to reflect user interactions.

    The WelcomeScreen class serves as the entry point to the game, setting the tone with a welcoming atmosphere and providing straightforward navigation to the game's core functionalities or customization settings.
    """

    def __init__(self, audio_manager):
        super().__init__(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.type = 'welcomeScreen'
        self.transitionToNextScreen = False
        self.options = False
        self.audio_manager = audio_manager

    def optionsChoice(self):
        print("transitioning to options screen")
        self.options = True            
        optionsDisplay = OptionsScreen(self.audio_manager)
        while (self.options == True):
            optionsDisplay.draw()
            optionsDisplay.handle_events()
            if (optionsDisplay.goBack == True):
                self.options = False
            pygame.display.flip()

    def choiceMade(self):
        print("transitioning from mainmenu to log in screen")
        self.transitionToNextScreen = True

    def draw(self):
        super().draw()
        # get the current width and height of the screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.buttons = [
            GameScreenButtons(self.width/5*2,self.height/3*2,200,40, "start", lambda: self.choiceMade(), self.WHITE, self.BLACK)
        ]
        self.optionsButton = GameScreenButtons(self.width/5*4, self.height/15*2, 150, 40, "Options", lambda: self.openOptions(), self.WHITE, self.BLACK)
        

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
        
        self.optionsButton.draw(self.screen)

        """
        potentially delete
        """
        pygame.draw.rect(self.screen,self.GREY,[self.width/844*17,self.height/600*7,30,30]) 

		# superimposing the text onto our button 
        self.screen.blit(self.welcome, (self.width/422*111,self.height/3))
        self.screen.blit(self.trivio, (self.width/2,self.height/2))
        """
        potentially delete
        """
        self.screen.blit(self.esc , (self.width/422*11,self.height/600))

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
                    button = pygame.Rect(self.width/844*322,self.height/3*2,200,40)

            for button in self.buttons:
                button.handle_event(event)
           
            """
            i dont think we need this on the welcome screen
            """
            # user clicking our exit button
            if event.type == pygame.MOUSEBUTTONDOWN: 
                #if the mouse is clicked on the x button the game is terminated 
                if self.width/844*17 <= self.mouse[0] <= self.width/844*17+30 and self.height/600*7 <=self.mouse[1] <= self.height/600*7+30:
                    pygame.quit()
                    sys.exit()

                self.optionsButton.handle_event(event)
                          

    def run(self):
        super().run()
