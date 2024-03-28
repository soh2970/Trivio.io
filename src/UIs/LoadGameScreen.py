import json
import sys
from src.UIs.screen import ScreenBase
from src.Player import Player
from src.UIs.GameScreenButtons import GameScreenButtons
import pygame
import os

class LoadGameScreen(ScreenBase):

    def __init__(self, player):
        super().__init__()
        self.type = "loadGameScreen"
        self.player = player
        self.currentSave = None
        self.continueButton = GameScreenButtons(self.screen.get_width()/2 - 80, self.screen.get_height()/2 + 180, 150, 40, "Continue?", lambda: self.handleContinue(), self.WHITE, self.BLACK)
        self.backButton = GameScreenButtons(self.screen.get_width()/2 - 400, self.screen.get_height()/2 - 270, 100, 40, "Back", lambda: self.handleBack(), self.WHITE, self.BLACK)
        self.back = False
        self.userContinue = False

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