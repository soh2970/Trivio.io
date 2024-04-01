import json
import pygame 
import sys
import os


# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)

# initializing the constructor 
pygame.init() 

# DISPLAY
# screen resolution 
initial_size = (844,600) 
screen = pygame.display.set_mode(initial_size, pygame.RESIZABLE) 
# constant sizes
MIN_WIDTH = 844
MIN_HEIGHT = 600 
# get width and height of screen
width = screen.get_width()
height = screen.get_height()
# fills the screen with a color: white 
white = (255,255,255)
screen.fill(white)
# set screen name
pygame.display.set_caption('Trivio')
# update game screen
pygame.display.update()

from src.UIs.screen import ScreenBase

class WinGameScreen(ScreenBase):
    """
	The screen that is shown when the player wins the game. It presents a congratulatory message two trophy images, and the final score of the player.

	Inherits from ScreenBase, utilizing its setup for a Pygame window/screen.

	Attributes:
		type (str): Identifier for the screen type, set to ‘winGameScreen’.
		score (int): The player's final score, passed to the class upon initialization.
		returnToMenu (bool): A boolean indicating whether the player has chosen to return to the main menu, initially set to False.

	Methods:
		__init__(self, score): 
            Initializes the win game screen with the player's score and basic settings.
		
        draw(self): 
            Renders the win screen, including two trophy images as visual feedback for winning, dynamic text displaying the player’s final score, and a congratulatory message. It also has a ’Next’ button, presumably to proceed to the next screen.
		
        handle_events(self): 
            Handles input events, such as window resizing, quitting the game, and detecting clicks on the "Next" button, updating returnToMenu to True upon a click.
		
        run(self): 
            Contains the main loop for handling events and rendering updates, inherited from ScreenBase.
		
        getSavedGame(self): 
            Attempts to load saved game data, indicating it also handles aspects of game progression or player achievements.
    """

    def __init__(self, score):
        super().__init__(self.MIN_WIDTH, self.MIN_HEIGHT)  # Initialize with ScreenBase settings
        self.score = score
        self.type = 'winGameScreen'
        self.returnToMenu = False

    def draw(self):
        super().draw()
        # get the current width and height of the screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        # Load the image
        # Since the Python file is in src/UI and the image is in src/image,
        # the relative path to the image is '../image/trophy.png'
        image_path = os.path.join('images', 'trophy.png')
        self.trophy_image = pygame.image.load(image_path)

        # Resize the image
        new_width, new_height = 300, 300  # New dimensions for the image
        self.trophy_image = pygame.transform.scale(self.trophy_image, (new_width, new_height))
        # Draw the trophy images
        self.screen.blit(self.trophy_image, (self.width/100*6, self.height/4))
        self.screen.blit(self.trophy_image, (self.width/10*6, self.height/4))

        # Create a rect for the "Next" button
        self.next_button = pygame.Rect(700, 550, 90, 30)

        # Draw the header text
        header_text = self.HEADING_FONT.render('WINNER', True, self.BLACK)
        self.screen.blit(header_text, (self.width/2-200, self.width/2-350))

        # Draw the congratulations message
        congrats_text = self.SMALLER_FONT.render('Congratulations on beating the boss!', True, self.BLACK)
        self.screen.blit(congrats_text, (self.width/2-200, self.width/2-250))
        stats_text = self.SMALLER_FONT.render('Here are your stats:', True, self.BLACK)
        self.screen.blit(stats_text, (self.width/2-110, self.width/2-200))

        # Draw the score change to self.score
        score_text = self.SMALLER_FONT.render(f'Final Score: {self.score}', True, self.BLACK)
        self.screen.blit(score_text, (self.width/2-90, self.width/2-150))

        # Draw the "Next" button
        pygame.draw.rect(self.screen, self.BLUE, self.next_button)
        button_text = self.SMALLER_FONT.render('Next', True, self.BLACK)
        self.screen.blit(button_text, (715, 555))

    def handle_events(self):
        # stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos() 
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.running = False
                    pygame.quit()
                    sys.exit()
                # user resizing screen
                elif event.type == pygame.VIDEORESIZE:
                    super().resize_screen(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the "Next" button was clicked
                    if self.next_button.collidepoint(event.pos):
                        self.returnToMenu = True

    def run(self):
        super().run()
    
    #fix this to get score of game
    def getSavedGame(self):
        # Correctly calculate the path to the playerBank.json file
        base_dir = os.path.dirname(os.path.dirname(__file__))  # This navigates up to the 'src' directory from 'src/UIs'
        json_path = os.path.join(base_dir, 'playerBank.json')  # Now, correctly points to 'src/playerBank.json'

        with open(json_path, "r") as file:
            data = json.load(file)
            if self.player.playerId in data:
                self.currentSave = data[self.player.playerId]["currentSavedGame"]
                return True
            else:
                return False


#initialize instance and run
if __name__ == '__main__':
    game_screen1 = WinGameScreen()
    game_screen1.run()