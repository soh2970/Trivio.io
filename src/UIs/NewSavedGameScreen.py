import sys
import os

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)

from .screen import ScreenBase
import pygame
# initializing the constructor
pygame.init()

class NewSavedGameScreen(ScreenBase):
    """
    A screen presented to the player offering the choice between starting a new game
    or loading a previously saved game. This screen is part of the initial setup
    and decision-making process for the player upon starting the game.

    Attributes:
        player (Player): The player instance, which may carry over saved player data if a game is loaded.
        type (str): Identifier for the screen type, set to 'newSavedGameScreen'.
        transitionToNewGame (bool): Flag indicating whether the player has chosen to start a new game.
        transitionToLoadGame (bool): Flag indicating whether the player has chosen to load a saved game.

    Methods:
        draw(self):
            Renders the screen elements, including options for new game and load game.

        handle_events(self):
            Processes input events such as button clicks, specifically detecting clicks on the new game or load game options.

        run(self):
            Contains the main loop for the NewSavedGameScreen, handling events and rendering updates.
    """
    def __init__(self, player=None):
        super().__init__()
        self.player = player
        self.type = 'newSavedGameScreen'
        self.transitionToNewGame = False
        self.transitionToLoadGame = False

    def draw(self):
        super().draw()
        # screen width and height
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        # text for buttons
        self.text_new_game = self.SMALLER_FONT.render('New Game', True, self.BLACK)
        self.text_saved_game = self.SMALLER_FONT.render('Saved Game', True, self.BLACK)
        self.text_esc = self.PARAGRAPH_FONT.render('x', True, self.BLACK)
        self.text_or = self.PARAGRAPH_FONT.render('OR',True, self.BLACK )

        # draw the buttons
        pygame.draw.circle(self.screen, self.GREEN, (self.width/4, self.height/2), 100)
        pygame.draw.circle(self.screen, self.BLUE, (3*self.width/4, self.height/2), 100)

        # put the text on the buttons
        self.screen.blit(self.text_new_game, (self.width/4 - self.text_new_game.get_width()/2, self.height/2 - self.text_new_game.get_height()/2))
        self.screen.blit(self.text_saved_game, (3*self.width/4 - self.text_saved_game.get_width()/2, self.height/2 - self.text_saved_game.get_height()/2))

        # draw close button
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-405,self.height/2-293,30,30])
        self.screen.blit(self.text_esc , (self.width/2-400,self.height/2-300))

        #put or on the screen
        self.screen.blit(self.text_or, (self.width/2-25, self.height/2-10))


    def handle_events(self):
        self.mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Calculate the distance from the click to the center of the "New Game" circle
                distance_to_new_game_circle = ((self.mouse[0] - self.width/4) ** 2 + (self.mouse[1] - self.height/2) ** 2) ** 0.5
                
                # Calculate the distance from the click to the center of the "Load Game" circle
                distance_to_load_game_circle = ((self.mouse[0] - 3*self.width/4) ** 2 + (self.mouse[1] - self.height/2) ** 2) ** 0.5
                
                # Check if the click was within the "New Game" circle
                if distance_to_new_game_circle < 100:  # Assuming the circle radius is 100
                    print("New game triggered!")
                    self.transitionToNewGame = True
                
                # Check if the click was within the "Load Game" circle
                elif distance_to_load_game_circle < 100:  # Assuming the circle radius is 100
                    print("Load game triggered!")
                    self.transitionToLoadGame = True

                # Close button click detection
                elif self.width/2-405 <= self.mouse[0] <= self.width/2-385 and self.height/2-293 <= self.mouse[1] <= self.height/2-263:
                    pygame.quit()

            # User resizing screen
            elif event.type == pygame.VIDEORESIZE:
                super().resize_screen(event)



    def run(self):
        super().run()

#initialize instance and run
if __name__ == '__main__':
    game_screen1 = NewSavedGameScreen()
    game_screen1.run()
