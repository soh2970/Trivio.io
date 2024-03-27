import sys
import os

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)

from Boss import Boss
from datetime import datetime
import json
import pygame
import sys
from src.Player import Player
from src.question2 import Question
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons
from src.UIs.CorrectAnswerScreen import CorrectAnswerScreen

class GameScreen(ScreenBase):

    def __init__(self, category, player, boss, question, level, score):
        super().__init__()
        self.startTime = pygame.time.get_ticks()
        self.boss = boss
        self.player = player
        self.level = level
        self.question = question
        self.correctAnswer = question.correctAnswer
        self.answered = False
        self.answeredCorrectly = None
        self.levelFont = pygame.font.SysFont('Corbel', 28)
        self.hpFont = pygame.font.SysFont('Corbel', 30)
        if len(question.prompt) > 50:
            self.promptFont = pygame.font.SysFont('Corbel', 25)
        else: self.promptFont = pygame.font.SysFont('Corbel', 40)
        self.buttons = [
            GameScreenButtons(self.screen.get_width()/2 - 273, self.screen.get_height()/2 + 90, 280, 100, question.choices[0], lambda: self.choiceMade(question.choices[0]), self.WHITE, self.BLACK),
            GameScreenButtons(self.screen.get_width()/2 - 273, self.screen.get_height()/2 + 192, 280, 100, question.choices[1], lambda: self.choiceMade(question.choices[1]), self.WHITE, self.BLACK),
            GameScreenButtons(self.screen.get_width()/2 + 9, self.screen.get_height()/2 + 90, 280, 100, question.choices[2], lambda: self.choiceMade(question.choices[2]), self.WHITE, self.BLACK),
            GameScreenButtons(self.screen.get_width()/2 + 9, self.screen.get_height()/2 + 192, 280, 100, question.choices[3], lambda: self.choiceMade(question.choices[3]), self.WHITE, self.BLACK),
        ]
        self.saveGameButton = GameScreenButtons(self.screen.get_width() / 2 + 200, self.screen.get_height() / 2 - 150, 150, 40, "Save Game", lambda: self.saveGame(), self.WHITE, self.BLACK)
        self.type = category
        self.score = score

    # logic for when user selects and answer
    def choiceMade(self, choice):
        if (choice == self.correctAnswer):
                self.boss.loseBossHP(self.level)
                print(f'bossHP = {self.boss.bossHp}')
                if (self.level == 1): self.score = self.score + 4
                elif (self.level == 2): self.score = self.score + 6
                elif (self.level == 3): self.score = self.score + 10
                self.answered = True
                self.answeredCorrectly = True
        else: 
            self.player.losePlayerHP(self.level)
            print(f'playerHP = {self.player.playerHP}')
            self.answered = True
            self.answeredCorrectly = False

        print(f'Score = {self.score}')


    #displays text, buttons, images on the screen 
    def draw(self):
        super().draw()

        #display current question prompt
        self.draw_text(self.question.prompt, self.promptFont, (255,0,0), self.screen, self.screen.get_width()/2 - 370, self.screen.get_height()/2 - 200)


        for button in self.buttons:
            button.draw(self.screen)

        self.saveGameButton.draw(self.screen)

        #display current level
        self.draw_text(f'Level: {str(self.level)}', self.levelFont, (255,0,0), self.screen, self.screen.get_width()/2 - 20, self.screen.get_height()/2 - 240)
        
        #display boss hp        
        self.draw_text(f'Boss HP: {str(self.boss.bossHp)}', self.hpFont, (255,0,0), self.screen, self.screen.get_width()/2 - 195, self.screen.get_height()/2 + 20)

        #display player hp
        self.draw_text(f'Player HP: {str(self.player.playerHP)}', self.hpFont, (255,0,0), self.screen, self.screen.get_width()/2 + 50, self.screen.get_height()/2 + 20)

        #display images based on boss and player hp  
        if (self.boss.bossHp <= 100 and self.boss.bossHp > 80):
            self.screen.blit(self.boss1_imageResized, (self.screen.get_width()/2 - 160, self.screen.get_height()/2 - 100))
        elif (self.boss.bossHp <= 80 and self.boss.bossHp > 50):
            self.screen.blit(self.boss2_imageResized, (self.screen.get_width()/2 - 160, self.screen.get_height()/2 - 100))
        elif (self.boss.bossHp <= 50 and self.boss.bossHp > 0):
            self.screen.blit(self.boss3_imageResized, (self.screen.get_width()/2 - 160, self.screen.get_height()/2 - 100))

        if (self.player.playerHP <= 100 and self.player.playerHP > 80):
            self.screen.blit(self.player1_imageResized, (self.screen.get_width()/2 + 80, self.screen.get_height()/2 - 100))
        elif (self.player.playerHP <= 80 and self.player.playerHP > 50):
            self.screen.blit(self.player2_imageResized, (self.screen.get_width()/2 + 80, self.screen.get_height()/2 - 100))
        elif (self.player.playerHP <= 50 and self.player.playerHP > 0):
            self.screen.blit(self.player3_imageResized, (self.screen.get_width()/2 + 80, self.screen.get_height()/2 - 100))
        elif (self.player.playerHP == 0):
            self.screen.blit(self.playerLose_imageResized, (self.screen.get_width()/2 + 80, self.screen.get_height()/2 - 100))
        
    #overridden from parent class
    def handle_events(self):
        for event in pygame.event.get():
            # user quits
            if event.type == pygame.QUIT: 
                self.running = False
                pygame.quit()
                sys.exit()

            # user resizing screen
            if event.type == pygame.VIDEORESIZE:
                super().resize_screen(event)
                self.saveGameButton.rect1 = pygame.Rect(self.screen.get_width() / 2 + 200, self.screen.get_height() / 2 - 150, 150, 40)
                self.saveGameButton.rect2 = pygame.Rect(self.screen.get_width() / 2 + 200, self.screen.get_height() / 2 - 150, 150, 40)
                for index, button in enumerate(self.buttons):
                    if (index == 0):
                        button.rect1 = pygame.Rect(self.screen.get_width()/2 - 273, self.screen.get_height()/2 + 90, 280, 100)
                        button.rect2 = pygame.Rect(self.screen.get_width()/2 - 273, self.screen.get_height()/2 + 90, 280, 100)
                    if (index == 1):
                        button.rect1 = pygame.Rect(self.screen.get_width()/2 - 273, self.screen.get_height()/2 + 192, 280, 100)
                        button.rect2 = pygame.Rect(self.screen.get_width()/2 - 273, self.screen.get_height()/2 + 192, 280, 100)
                    if (index == 2):
                        button.rect1 = pygame.Rect(self.screen.get_width()/2 + 9, self.screen.get_height()/2 + 90, 280, 100)
                        button.rect2 = pygame.Rect(self.screen.get_width()/2 + 9, self.screen.get_height()/2 + 90, 280, 100)
                    if (index == 3):
                        button.rect1 = pygame.Rect(self.screen.get_width()/2 + 9, self.screen.get_height()/2 + 192, 280, 100)
                        button.rect2 = pygame.Rect(self.screen.get_width()/2 + 9, self.screen.get_height()/2 + 192, 280, 100)

            #handle button logic
            if (event.type == pygame.MOUSEBUTTONDOWN):
                for button in self.buttons:
                    button.handle_event(event)
                self.saveGameButton.handle_event(event)                
                


    #draws text onto the screen
    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def saveGame(self):
        datetime_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        gameState = {
            "timeStamp": datetime_string,
            "levelAchieved": f'{self.level}',
            "subject": f'{self.type}',
            "score":f'{self.score}',
            "playerHP": f'{self.player.playerHP}',
            "bossHP": f'{self.boss.bossHp}'
        }

        with open("src/playerBank.json", "r+") as file:
            data = json.load(file)
            if self.player.playerId in data:
                data[self.player.playerId]['currentSavedGame'] = gameState
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                print("saved Game")
            else: raise Exception("Player not found in database")

            


    # Load the boss level1 image
    boss1_image_path = 'images/level1MathApple.png'
    boss1_image = pygame.image.load(boss1_image_path)
    boss1_imageResized = pygame.transform.scale(boss1_image, (80,80))

    # Load the boss level2 image
    boss2_image_path = 'images/level2MathApple.png'
    boss2_image = pygame.image.load(boss2_image_path)
    boss2_imageResized = pygame.transform.scale(boss2_image, (80,80))

    #load the boss level3 image
    boss3_image_path = 'images/level3MathApple.png'
    boss3_image = pygame.image.load(boss3_image_path)
    boss3_imageResized = pygame.transform.scale(boss3_image, (80,80))

    #load the player level1 image
    player1_image_path = 'images/userLevel1.png'
    player1_image = pygame.image.load(player1_image_path)
    player1_imageResized = pygame.transform.scale(player1_image, (80,80))

    #load the player level2 image
    player2_image_path = 'images/userLevel2.png'
    player2_image = pygame.image.load(player2_image_path)
    player2_imageResized = pygame.transform.scale(player2_image, (80,80))

    #load the player level3 image
    player3_image_path = 'images/userLevel3.png'
    player3_image = pygame.image.load(player3_image_path)
    player3_imageResized = pygame.transform.scale(player3_image, (80,80))

    #load the player lose image
    playerLose_image_path = 'images/userLose.jpeg'
    playerLose_image = pygame.image.load(playerLose_image_path)
    playerLose_imageResized = pygame.transform.scale(playerLose_image, (80,80))

