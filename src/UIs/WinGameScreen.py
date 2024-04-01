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
    Represents the victory screen displayed when a player wins the game, featuring celebratory messages,
    trophy imagery to symbolize the victory, and a display of the player's final score. This screen is part
    of the game's flow, marking the completion of the game with a positive acknowledgment of the player's success.

    Inherits from ScreenBase, making use of its foundational setup for a Pygame window/screen, including handling
    resizing and basic event management.

    Attributes:
        score (int): The player's final score, which is displayed on the screen.
        type (str): Identifier for the screen type, set to 'winGameScreen'.
        transitionToLeaderboard (bool): Flag indicating whether to transition to the leaderboard screen,
            typically activated when the player clicks the "Next" button.

    Methods:
        __init__(self, score): 
            Constructor for initializing the win game screen with the player's final score.
        
        draw(self): 
            Renders the victory screen, showing trophy images, congratulatory text, player's final score,
            and a "Next" button for proceeding.
        
        handle_events(self): 
            Processes input events such as clicking the "Next" button, resizing the window, and closing the game.
            Transitions to the leaderboard screen upon clicking "Next".
        
        run(self): 
            Executes the main loop for the win game screen, handling events and updating the display.
        
        getSavedGame(self): 
            Loads saved game data, potentially for displaying progress or achievements leading up to the win. This method
            suggests the presence of saved game management, though its relevance to the win screen's primary function appears limited.
    """

    def __init__(self, score):
        super().__init__(self.MIN_WIDTH, self.MIN_HEIGHT)  # Initialize with ScreenBase settings
        self.score = score
        self.type = 'winGameScreen'
        self.transitionToLeaderboard = False

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
                        self.transitionToLeaderboard = True

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