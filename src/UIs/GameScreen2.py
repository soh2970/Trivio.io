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
#from src.UIs.OptionsScreen import OptionsScreen
from src.Player import Player
from src.question2 import Question
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons
from src.UIs.CorrectAnswerScreen import CorrectAnswerScreen
from src.UIs.OptionsScreen import OptionsScreen

from src.UIs.WinLevelScreen import WinLevelScreen

images_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'images')

class GameScreen(ScreenBase):
    """
    Facilitates the main gameplay interface in a Pygame application, where players engage with questions, 
    answer them, and see immediate effects on the game's dynamics, including changes to player and boss health
    based on the correctness of answers. This screen is where the core gameplay unfolds, with the player navigating
    through questions of varying difficulty across different educational categories.

    Attributes:
        startTime (datetime): The timestamp marking the beginning of the game session.
        boss (Boss): Instance of Boss class, representing the adversary in the game, with its health points.
        player (Player): Instance of Player class, representing the user's avatar in the game, with its health points.
        level (int): Current difficulty level of the game, affecting the complexity of questions and damage mechanics.
        question (Question): The current question object presented to the player.
        correctAnswer (str): The correct answer for the current question, used for validation.
        answered (bool): Flag to check if the current question has been answered.
        answeredCorrectly (bool or None): Indicates the correctness of the player's last answer; True if correct.
        levelFont, hpFont, promptFont (pygame.font.Font): Custom fonts for displaying game information (level, health points, question prompts).
        buttons (list of GameScreenButtons): Interactive buttons for each of the multiple-choice answers.
        saveGameButton (GameScreenButtons): Button to save the current game state.
        type (str): The category of the current question being asked.
        score (int): The player's current score, updated based on performance.
        audio_manager: Manages game audio, including background music and sound effects.
        questions_correct, questions_incorrect (int): Counters for the number of questions answered correctly and incorrectly.
        goToMain (bool): Flag for navigating back to the main menu.
        showSaveFeedback (bool): Indicates whether feedback for a game save operation should be displayed.
        saveFeedbackTimer (int): Timer to control the display duration of the save feedback message.

    Methods:
        choiceMade(self, choice): Processes the player's answer, updating game state based on correctness.
        draw(self): Renders all game elements on the screen, including question text, answer buttons, and player/boss HP.
        handle_events(self): Handles user input, including answer selection and navigation.
        draw_text(self, text, font, color, surface, x, y): Utility method for drawing text on the screen.
        saveGame(self): Serializes the current game state to a file for later retrieval.
        endGame(self): Concludes the game session, potentially saving final scores and transitioning to an end game screen.
        displaySaveFeedback(self): Temporarily displays a save confirmation message on the screen.
        openOptions(self): Transitions to the options screen for game settings adjustments.
        toMainScreen(self): Flags the screen to return to the main menu.
    """

    def __init__(self, category, player, boss, question, level, score, audio_manager, questions_correct, questions_incorrect, width, height):
        super().__init__(width, height)
        
        self.startTime = pygame.time.get_ticks()
        self.boss = boss
        self.player = player
        self.level = level
        self.question = question
        self.correctAnswer = question.correctAnswer
        self.answered = False
        self.answeredCorrectly = None
        self.transitionToOptions = False
        self.levelFont = self.LEVEL_FONT
        self.hpFont = self.HP_FONT
        if len(question.prompt) > 50:
            self.promptFont = self.LEVEL_FONT
        else: self.promptFont = self.MID_FONT
        self.type = category
        self.score = score
        self.audio_manager = audio_manager
        self.options = False
        self.questions_correct = questions_correct
        self.questions_incorrect = questions_incorrect
        self.goToMain = False
        self.showSaveFeedback = False
        self.saveFeedbackTimer = 0

    def displaySaveFeedback(self):
        self.showSaveFeedback = True
        self.saveFeedbackTimer = pygame.time.get_ticks()

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

    def toMainScreen(self):
        self.goToMain = True


    #displays text, buttons, images on the screen
    def draw(self):
        super().draw()

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        if self.showSaveFeedback:
            current_time = pygame.time.get_ticks()
            if current_time - self.saveFeedbackTimer < 2000:  # Display the message for 2 seconds
                self.draw_text("Game Saved!", self.promptFont, (0, 255, 0), self.screen, 20,70)
            else:
                self.showSaveFeedback = False


        # Define the relative size for each button
        button_width = self.width * 0.3
        button_height = self.height * 0.15

        # Define spacing between buttons and between rows
        spacing = self.width * 0.02  # Space between buttons
        vertical_spacing = self.height* 0.02  # Space between rows
        
        # Calculate total width of two buttons including spacing
        total_buttons_width = (button_width * 2) + spacing
        
        # Determine the starting x coordinate for the first button to center the group horizontally
        start_x = (self.width - total_buttons_width) / 2

        # Determine the starting y coordinate for the first row to place the group near the bottom
        start_y = self.height - (button_height * 2) - vertical_spacing - (self.height * 0.05)  # 5% from the bottom
        
        # Create and position each button, with two buttons per row
        self.buttons = []
        for i in range(4):
            # Calculate x position for the current button
            row = i // 2  # Determine row index (0 or 1)
            col = i % 2  # Determine column index (0 or 1)
            button_x = start_x + col * (button_width + spacing)
            button_y = start_y + row * (button_height + vertical_spacing)
            
            # Instantiate the button and add it to the list
            button = GameScreenButtons(
                button_x, 
                button_y, 
                button_width, 
                button_height,
                self.question.choices[i], 
                lambda i=i: self.choiceMade(self.question.choices[i]),
                self.WHITE, 
                self.BLACK
            )
            self.buttons.append(button)


        self.saveGameButton = GameScreenButtons(self.width/5*4, self.height/15*1, 150, 40, "Save Game", lambda: self.saveGame(), self.WHITE, self.BLACK)
        self.optionsButton = GameScreenButtons(self.width/5*4, self.height/15*2, 150, 40, "Options", lambda: self.openOptions(), self.WHITE, self.BLACK)

        self.toMainButton = GameScreenButtons(20, 20, 100, 40, 'To Main', lambda: self.toMainScreen(), self.WHITE, self.BLACK)

        #display current question prompt
        # make it a text rect
        self.text1 = self.promptFont.render(self.question.prompt, True, self.BLACK)
        self.textRect1 = self.text1.get_rect(center = (self.width/2, self.height/12*3))
        self.screen.blit(self.text1, self.textRect1)

        for button in self.buttons:
            button.draw(self.screen)

        self.saveGameButton.draw(self.screen)
        self.optionsButton.draw(self.screen)
        self.toMainButton.draw(self.screen)

        #display current level
        # self.draw_text(f'Level: {str(self.level)}', self.levelFont, (255,0,0), self.screen, self.width/2, self.height/20)
         # make it a text rect
        self.level_text = self.levelFont.render(f'Level: {str(self.level)}', True, (255,0,0))
        self.level_textRect = self.level_text.get_rect(center = (self.width//2, self.height/12))
        self.screen.blit(self.level_text, self.level_textRect)
        
        #display boss hp
        # self.draw_text(f'Boss HP: {str(self.boss.bossHp)}', self.hpFont, (255,0,0), self.screen, self.width/5*2, self.height/20*5)
         # make it a text rect
        self.boss_text = self.hpFont.render(f'Boss HP: {str(self.boss.bossHp)}', True, (255,0,0))
        self.boss_textRect = self.boss_text.get_rect(center = (self.width/15*5, self.height/20*12))
        self.screen.blit(self.boss_text, self.boss_textRect)

        #display player hp
        # self.draw_text(f'Player HP: {str(self.player.playerHP)}', self.hpFont, (255,0,0), self.screen, self.width/5*4, self.height/20*5)
         # make it a text rect
        self.player_text = self.hpFont.render(f'Player HP: {str(self.player.playerHP)}', True, (255,0,0))
        self.player_textRect = self.player_text.get_rect(center = (self.width/15*10, self.height/20*12))
        self.screen.blit(self.player_text, self.player_textRect)

        #display images based on boss and player hp
        if (self.boss.bossHp <= 100 and self.boss.bossHp > 80):
            self.screen.blit(self.boss1_imageResized, (self.width/15*5, self.height/20*8))
        elif (self.boss.bossHp <= 80 and self.boss.bossHp > 50):
            self.screen.blit(self.boss2_imageResized, (self.width/15*5, self.height/20*8))
        elif (self.boss.bossHp <= 50 and self.boss.bossHp > 0):
            self.screen.blit(self.boss3_imageResized, (self.width/15*5, self.height/20*8))

        if (self.player.playerHP <= 100 and self.player.playerHP > 80):
            self.screen.blit(self.player1_imageResized, (self.width/15*9.5, self.height/20*8))
        elif (self.player.playerHP <= 80 and self.player.playerHP > 50):
            self.screen.blit(self.player2_imageResized, (self.width/15*9.5, self.height/20*8))
        elif (self.player.playerHP <= 50 and self.player.playerHP > 0):
            self.screen.blit(self.player3_imageResized, (self.width/15*9.5,self.height/20*8))
        elif (self.player.playerHP == 0):
            self.screen.blit(self.playerLose_imageResized, (self.width/15*9.5, self.height/20*8))
        
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

                '''
                self.saveGameButton.rect1 = pygame.Rect(self.screen.get_width() / 2 + 200, self.screen.get_height() / 2 - 150, 150, 40)
                self.saveGameButton.rect2 = pygame.Rect(self.screen.get_width() / 2 + 200, self.screen.get_height() / 2 - 150, 150, 40)

                self.optionsButton.rect1 = pygame.Rect(self.screen.get_width() / 2 + 200, self.screen.get_height() / 2 - 100, 150, 40)
                self.optionsButton.rect2 = pygame.Rect(self.screen.get_width() / 2 + 200, self.screen.get_height() / 2 - 100, 150, 40)

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
'''
            
            
            #handle button logic
            if (event.type == pygame.MOUSEBUTTONDOWN):
                for button in self.buttons:
                    button.handle_event(event)
                self.saveGameButton.handle_event(event)
                self.optionsButton.handle_event(event)
                self.toMainButton.handle_event(event)


    #draws text onto the screen
    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def openOptions(self):
        print("transitioning to options screen")
        self.options = True            
        optionsDisplay = OptionsScreen(self.audio_manager, self.width, self.height)
        while (self.options == True):
            optionsDisplay.draw()
            optionsDisplay.handle_events()
            if (optionsDisplay.goBack == True):
                self.options = False
            pygame.display.flip()

    def saveGame(self):
        datetime_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        gameState = {
            "timeStamp": datetime_string,
            "levelAchieved": str(self.level),
            "subject": self.type,
            "score": int(self.score),
            "playerHP": str(self.player.playerHP),
            "bossHP": str(self.boss.bossHp),
            "questions_correct": self.questions_correct,
            "questions_incorrect": self.questions_incorrect
        }

        # Correctly calculate the path to the playerBank.json file
        base_dir = os.path.dirname(os.path.dirname(__file__))  # This navigates up to the 'src' directory from 'src/UIs'
        json_path = os.path.join(base_dir, 'playerBank.json')  # Now, correctly points to 'src/playerBank.json'

        with open(json_path, "r+") as file:
            data = json.load(file)
            if self.player.playerId in data:
                data[self.player.playerId]['currentSavedGame'] = gameState
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                print("Game saved")
                self.displaySaveFeedback()
            else:
                raise Exception("Player not found in database")


    """ method will end the game if user HP is 0 or Boss Hp is 0"""            
    def endGame(self):
        datetime_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if (self.player.playerHP > 0):
            finalScore = self.player.playerHP * self.score 
        else: finalScore = self.score       


        # Correctly calculate the path to the playerBank.json file
        base_dir = os.path.dirname(os.path.dirname(__file__))  # This navigates up to the 'src' directory from 'src/UIs'
        json_path = os.path.join(base_dir, 'playerBank.json')  # Now, correctly points to 'src/playerBank.json'

        with open(json_path, "r+") as file:
            data = json.load(file)
            if self.player.playerId in data:

                if data[self.player.playerId]['highscore'] < finalScore:
                    data[self.player.playerId]['highscore'] = finalScore
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                print("Game Ended")
            else:
                raise Exception("Player not found in database")

            


    # Load the boss level1 image
    boss1_image_path = os.path.join(images_dir, 'level1MathApple.png')
    boss1_image = pygame.image.load(boss1_image_path)
    boss1_imageResized = pygame.transform.scale(boss1_image, (80,80))

    # Load the boss level2 image
    boss2_image_path = os.path.join(images_dir, 'level2MathApple.png')
    boss2_image = pygame.image.load(boss2_image_path)
    boss2_imageResized = pygame.transform.scale(boss2_image, (80,80))

    #load the boss level3 image
    boss3_image_path = os.path.join(images_dir, 'level3MathApple.png')
    boss3_image = pygame.image.load(boss3_image_path)
    boss3_imageResized = pygame.transform.scale(boss3_image, (80,80))

    #load the player level1 image
    player1_image_path = os.path.join(images_dir, 'userLevel1.png')
    player1_image = pygame.image.load(player1_image_path)
    player1_imageResized = pygame.transform.scale(player1_image, (80,80))

    #load the player level2 image
    player2_image_path = os.path.join(images_dir, 'userLevel2.png')
    player2_image = pygame.image.load(player2_image_path)
    player2_imageResized = pygame.transform.scale(player2_image, (80,80))

    #load the player level3 image
    player3_image_path = os.path.join(images_dir, 'userLevel3.png')
    player3_image = pygame.image.load(player3_image_path)
    player3_imageResized = pygame.transform.scale(player3_image, (80,80))

    #load the player lose image
    playerLose_image_path = os.path.join(images_dir, 'userLose.jpeg')
    playerLose_image = pygame.image.load(playerLose_image_path)
    playerLose_imageResized = pygame.transform.scale(playerLose_image, (80,80))


#initialize instance and run
if __name__ == '__main__':
    game_screen1 = GameScreen()
    game_screen1.run()