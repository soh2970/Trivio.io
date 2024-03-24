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

    def __init__(self, category, player, question):
        super().__init__()
        self.boss = Boss()
        self.player = Player("natetyu", 100, 0, 1)
        self.question = question
        self.buttons = [
            GameScreenButtons(150, 400, 200, 50, question.choices[0], lambda: self.choiceMade(question.choices[0])),
            GameScreenButtons(150, 500, 200, 50, question.choices[1], lambda: self.choiceMade(question.choices[1])),
            GameScreenButtons(450, 400, 200, 50, question.choices[2], lambda: self.choiceMade(question.choices[2])),
            GameScreenButtons(450, 500, 200, 50, question.choices[3], lambda: self.choiceMade(question.choices[3])),
        ]


    def choiceMade(self, choice):
        print(choice)

    def display(self, screen):
        screen.fill((255,255,255))

        for button in self.buttons:
            button.draw(screen)

        if (self.boss.bossHp <= 100 and self.boss.bossHp >= 80):
            screen.blit(self.boss1_imageResized, (200, 200))
        elif (self.boss.bossHp <= 79 and self.boss.bossHp >= 50):
            screen.blit(self.boss2_imageResized, (200, 200))
        elif (self.boss.bossHp <= 50 and self.boss.bossHp > 0):
            screen.blit(self.boss3_imageResized, (200, 200))

        if (self.player.playerHP <= 100 and self.player.playerHP >= 80):
            screen.blit(self.player1_imageResized, (500, 200))
        elif (self.player.playerHP <= 79 and self.player.playerHP >= 50):
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


    #Font setup
    # font = pygame.font.Font(None, 36)

    # # Function to draw text
    # def draw_text(self, text, font, color, surface, x, y):
    #     textobj = font.render(text, 1, color)
    #     textrect = textobj.get_rect()
    #     textrect.topleft = (x, y)
    #     surface.blit(textobj, textrect)

    # # """
    # # Set up Boss and Player
    # # """





    # """
    # Hardcoded question to be displayed
    # """
    # q = Question(1, "What is the perimeter of a rectangle with diagonal length 17 units and length 8 units?", ["1","2","3","4"], "2", 4, False, "Math")

    # # Function to draw buttons and check for clicks
    # def draw_button(self, text, x, y, width, height, action=None):
    #     mouse = pygame.mouse.get_pos()
    #     click = pygame.mouse.get_pressed()
    #     button_rect = pygame.Rect(x, y, width, height)

    #     if button_rect.collidepoint(mouse):
    #         pygame.draw.rect(screen, GREEN, button_rect)
    #         if click[0] == 1 and action is not None:
    #             action()
    #     else:
    #         pygame.draw.rect(screen, WHITE, button_rect)

    #     draw_text(text, font, BLACK, screen, x + 10, y + 10)

    # def check_answer(self, answer):
    #     if answer == q.correctAnswer:
    #         print("Correct!")
    #     else:
    #         print("Incorrect!")

    # # Main game loop
    # # running = True
    # # while running:
    # #     screen.fill(WHITE)
        
    # #     # Event loop
    # #     for event in pygame.event.get():
    # #         if event.type == pygame.QUIT:
    # #             running = False

    #     """
    #     Check what level hp boss is and render image accordingly
    #     """


    #     """
    #     Check what level hp player is and render image accordingly
    #     """



    #     """
    #     Check if length of string can fit in the window, if not then lower font size
    #     """
    #     if (len(q.prompt) > 50):
    #         font = pygame.font.Font(None, 24)
        
    #     # Draw question
    #     draw_text(q.prompt, font, BLACK, screen, 100, 100)
        
    #     # Draw answer buttons
    #     for i, answer in enumerate(q.choices):
    #         button_x = 100 + (i % 2) * 300
    #         button_y = 400 + (i // 2) * 100
    #         draw_button(answer, button_x, button_y, 200, 50, lambda a=answer: check_answer(a))

    #     pygame.display.flip()

    # pygame.quit()
    # sys.exit()
