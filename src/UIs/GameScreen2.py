import sys
import os

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)

import pygame
import sys
from src.Boss import Boss
from Player import Player
from question2 import Question
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons

class GameScreen(ScreenBase):

    def __init__(self, category, player, boss, question, level):
        super().__init__()
        self.startTime = pygame.time.get_ticks()
        self.boss = boss
        self.player = player
        self.level = level
        self.question = question
        self.correctAnswer = question.correctAnswer
        self.answered = False
        self.levelFont = pygame.font.SysFont('Corbel', 28)
        self.hpFont = pygame.font.SysFont('Corbel', 30)
        if len(question.prompt) > 50:
            self.promptFont = pygame.font.SysFont('Corbel', 25)
        else: self.promptFont = pygame.font.SysFont('Corbel', 40)
        self.buttons = [
            GameScreenButtons(150, 390, 280, 100, question.choices[0], lambda: self.choiceMade(question.choices[0])),
            GameScreenButtons(150, 495, 280, 100, question.choices[1], lambda: self.choiceMade(question.choices[1])),
            GameScreenButtons(435, 390, 280, 100, question.choices[2], lambda: self.choiceMade(question.choices[2])),
            GameScreenButtons(435, 495, 280, 100, question.choices[3], lambda: self.choiceMade(question.choices[3])),
        ]
        self.type = category

    # logic for when user selects and answer
    def choiceMade(self, choice):
        if (choice == self.correctAnswer):
                self.boss.loseBossHP(self.level)
                print(f'bossHP = {self.boss.bossHp}')
                self.answered = True
        else: 
            self.player.losePlayerHP(self.level)
            print(f'playerHP = {self.player.playerHP}')
            self.answered = True


    #displays text, buttons, images on the screen 
            
    def display(self, screen):

        screen.fill((255,255,255))

        #display current question prompt
        self.draw_text(self.question.prompt, self.promptFont, (255,0,0), screen, 50, 100)

        # displays the current elapsed time
        elapsed_time = (pygame.time.get_ticks() - self.startTime) // 1000  # Convert milliseconds to seconds

        # Convert seconds to minutes and seconds
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60

        if minutes == 0:
            time_text = f'Time: {seconds} seconds'
        else:
            time_text = f'Time: {minutes} minute(s) {seconds} seconds'

        self.draw_text(time_text, self.levelFont, (255, 0, 0), screen, 600, 40)

        for button in self.buttons:
            button.draw(screen)

        #display current level
        self.draw_text(f'Level: {str(self.level)}', self.levelFont, (255,0,0), screen, 380, 40)
        
        #display boss hp        
        self.draw_text(f'Boss HP: {str(self.boss.bossHp)}', self.hpFont, (255,0,0), screen, 225, 320)

        #display player hp
        self.draw_text(f'Player HP: {str(self.player.playerHP)}', self.hpFont, (255,0,0), screen, 470, 320)

        #display images based on boss and player hp  
        if (self.boss.bossHp <= 100 and self.boss.bossHp > 80):
            screen.blit(self.boss1_imageResized, (250, 200))
        elif (self.boss.bossHp <= 80 and self.boss.bossHp > 50):
            screen.blit(self.boss2_imageResized, (250, 200))
        elif (self.boss.bossHp <= 50 and self.boss.bossHp > 0):
            screen.blit(self.boss3_imageResized, (250, 200))

        if (self.player.playerHP <= 100 and self.player.playerHP > 80):
            screen.blit(self.player1_imageResized, (500, 200))
        elif (self.player.playerHP <= 80 and self.player.playerHP > 50):
            screen.blit(self.player2_imageResized, (500, 200))
        elif (self.player.playerHP <= 50 and self.player.playerHP > 0):
            screen.blit(self.player3_imageResized, (500, 200))
        elif (self.player.playerHP == 0):
            screen.blit(self.playerLose_imageResized, (500, 200))
        
    #overridden from parent class
    def handle_events(self):
        for event in pygame.event.get():
            # user quits
            if event.type == pygame.QUIT: 
                self.running = False
                pygame.quit()
                sys.exit()
            # user resizing screen
            elif event.type == pygame.VIDEORESIZE:
                self.resize_screen(event)
            for button in self.buttons:
                button.handle_event(event)

    #draws text onto the screen
    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


        

            


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