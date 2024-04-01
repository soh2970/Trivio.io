import json
import sys
from src.UIs.screen import ScreenBase
from src.Player import Player
from src.UIs.GameScreenButtons import GameScreenButtons
import pygame
import os

class LoadGameScreen(ScreenBase):
    """
    Facilitates loading of a previously saved game state for a player in a Pygame application, presenting the player
    with their saved progress including level, score, and health status. This screen is integral for games that offer
    long-term progression, allowing players to return to their last checkpoint rather than starting anew each session.

    Inherits from ScreenBase to utilize core screen management and rendering capabilities, integrating seamlessly with
    the application's overall UI/UX design.

    Attributes:
        type (str): Identifier for the screen, facilitating screen management within the application.
        player (Player): The current player instance, whose game state is to be loaded.
        currentSave (dict or None): Loaded save data, including game progress and player stats.
        continueButton (GameScreenButtons): A button enabling the player to proceed with the loaded game state.
        backButton (GameScreenButtons): A button for returning to the previous screen, typically the main menu.
        back (bool): Indicates the player's decision to return to the previous screen.
        userContinue (bool): Indicates the player's decision to proceed with the loaded game.
        questions_correct (int): Number of questions the player answered correctly in the saved game.
        questions_incorrect (int): Number of questions the player answered incorrectly in the saved game.

    Methods:
        handleContinue(self):
            Marks the player's choice to continue with the saved game, setting `userContinue` to true.

        handleBack(self):
            Marks the player's choice to return to the previous screen, setting `back` to true.

        draw(self):
            Renders the screen with the saved game details and interactive buttons for game continuation or return.

        handle_events(self):
            Handles user inputs, detecting interactions with the `continueButton` and `backButton`.

        getSavedGame(self):
            Retrieves and loads the player's saved game data from a file, updating `currentSave` with the fetched data.

    This class plays a crucial role in enhancing player engagement and retention by enabling seamless continuation of gameplay
    across multiple sessions, contributing to a user-friendly and satisfying game experience.
    """
    def __init__(self, player):
        super().__init__(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.type = "loadGameScreen"
        self.player = player
        self.currentSave = None
        self.continueButton = GameScreenButtons(self.screen.get_width()/2 - 80, self.screen.get_height()/2 + 180, 150, 40, "Continue?", lambda: self.handleContinue(), self.WHITE, self.BLACK)
        self.backButton = GameScreenButtons(self.screen.get_width()/2 - 400, self.screen.get_height()/2 - 270, 100, 40, "Back", lambda: self.handleBack(), self.WHITE, self.BLACK)
        self.back = False
        self.userContinue = False
        self.questions_correct = 0
        self.questions_incorrect = 0

    def handleContinue(self):
        print("user wants to continue")
        self.userContinue = True

    def handleBack(self):
        print("user wants to go BAcK")
        self.back = True

    def draw(self):
        super().draw()
        if (self.getSavedGame() == True):
            #draw header text
            text_surface = self.MODE_SELECT_FONT.render(f'Current Saved Game for {self.player.playerId}', True, self.BLACK)
            self.screen.blit(text_surface, (100,130))

            #draw saved date text
            date = self.currentSave['timeStamp']
            text_surface = self.MODE_SELECT_FONT.render(f'Date = {date}', True, self.BLACK)
            self.screen.blit(text_surface, (200,200))

            #draw saved level data
            currentLevel = self.currentSave['levelAchieved']
            text_surface = self.MODE_SELECT_FONT.render(f'Current Level = {currentLevel}', True, self.BLACK)
            self.screen.blit(text_surface, (200,240))

            #draw saved category data
            category = self.currentSave['subject']
            text_surface = self.MODE_SELECT_FONT.render(f'Category = {category}', True, self.BLACK)
            self.screen.blit(text_surface, (200,280))

            #draw saved score data
            score = self.currentSave['score']
            text_surface = self.MODE_SELECT_FONT.render(f'Score = {score}', True, self.BLACK)
            self.screen.blit(text_surface, (200,320))

            #draw saved playerHP data
            playerHP = self.currentSave['playerHP']
            text_surface = self.MODE_SELECT_FONT.render(f'Player HP = {playerHP}', True, self.BLACK)
            self.screen.blit(text_surface, (200,360))

            #draw saved bossHP data
            bossHP = self.currentSave['bossHP']
            text_surface = self.MODE_SELECT_FONT.render(f'Boss HP = {bossHP}', True, self.BLACK)
            self.screen.blit(text_surface, (200,400))

            #logic for getting questions_correct and questions_incorrect
            self.questions_correct = self.currentSave['questions_correct']
            self.questions_incorrect = self.currentSave['questions_incorrect']

            #draw continue button
            self.continueButton.draw(self.screen)

            #draw back button
            self.backButton.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            # user quits
            if event.type == pygame.QUIT: 
                self.running = False
                pygame.quit()
                sys.exit()
            # user resizing screen
            if event.type == pygame.VIDEORESIZE:
                self.resize_screen(event)  
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.continueButton.handle_event(event)
                self.backButton.handle_event(event)


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