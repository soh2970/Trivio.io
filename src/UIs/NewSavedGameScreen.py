import sys
import os
from src.UIs.GameScreenButtons import GameScreenButtons
from src.UIs.screen import ScreenBase



# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)

import pygame
# initializing the constructor
pygame.init()

class NewSavedGameScreen(ScreenBase):
    """
    Presents the player with the option to start a new game or load an existing game from a saved state,
    offering a straightforward navigation point at the beginning of the game session. Additionally, this screen
    provides access to view the game's leaderboard.

    Inherits from ScreenBase, leveraging general screen setup and event handling while implementing specific
    functionalities for game state selection.

    Attributes:
        player (Player, optional): The player instance, potentially carrying over data if a game is loaded.
        type (str): Screen identifier, used to manage different screens within the application.
        transitionToNewGame (bool): Indicates the player's decision to start a new game.
        transitionToLoadGame (bool): Indicates the player's decision to load a saved game.
        transitionToLeaderboard (bool): Indicates the player's decision to view the leaderboard.
        leaderBbutton (GameScreenButtons): Button that transitions the player to the leaderboard screen.

    Methods:
        on_leaderboard(self):
            Handles the transition to the leaderboard screen upon button interaction.

        draw(self):
            Renders the screen's UI elements, including interactive buttons for new game, load game, and leaderboard options.

        handle_events(self):
            Processes input events, detecting clicks on new game, load game, or leaderboard buttons, and triggers the corresponding actions.

        run(self):
            Manages the main event loop for the screen, handling events and rendering updates to provide a responsive UI for game state selection.

    The NewSavedGameScreen class acts as an initial decision point for players, facilitating seamless game state management
    and enhancing the game's accessibility and user engagement.
    """
    def __init__(self, current_width, current_height, player=None):
        super().__init__(current_width, current_height)
        self.player = player
        self.type = 'newSavedGameScreen'
        self.transitionToNewGame = False
        self.transitionToLoadGame = False
        self.transitionToLeaderboard = False
        self.leaderBbutton = GameScreenButtons(60, 10, 100, 40, 'Scores', self.on_leaderboard, (220, 220, 220), (0,0,0))

    def on_leaderboard(self):
        print("leaderboard clicked!")
        self.transitionToLeaderboard = True


    def draw(self):
        super().draw()
        # screen width and height
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.leaderBbutton.draw(self.screen)

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

                elif self.leaderBbutton.button.collidepoint(event.pos):
                    self.leaderBbutton.callback()

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
