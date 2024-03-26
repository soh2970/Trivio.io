import pygame
from src.UIs.screen import ScreenBase
from src.UIs.GameScreen2 import GameScreen
from src.question2 import Question
from question2 import Question
from Level import Level
from Player import Player
from Boss import Boss
from game import Game
from MainMenu import MainMenu
from src.UIs.GameModeSelectScreen import GameModeSelectScreen
from src.UIs.WelcomeScreen import WelcomeScreen
from src.UIs.LoginScreen import LoginScreen


def run_game():

    running = True
    screen = pygame.display.set_mode((844,600), pygame.RESIZABLE)
    clock = pygame.time.Clock()



    current_player = None
    boss = Boss()
    current_screen = WelcomeScreen()
    level = Level(1, 'science')
    

    while running:
        
        #initial welcome screen
        if (current_screen.type == 'welcomeScreen'):
            current_screen.draw()
            current_screen.handle_events()
            if (current_screen.transitionToNextScreen): current_screen = LoginScreen()

        #login screen logic
        if (current_screen.type == 'loginScreen'):
            current_screen.draw()
            current_screen.handle_events()
            if (current_screen.isValidUser):
                current_player = current_screen.Player
                current_screen = MainMenu(current_player)
                print(current_player.playerId)

        #main menu logic
        if (current_screen.type == "mainMenu"):
            current_screen.display(screen)
            if (current_screen.handle_events() == 0):
                print("transitioning to category select screen")
                current_screen = GameModeSelectScreen()
        
        #game mode selection logic
        if (current_screen.type == 'gameModeSelect'):
            current_screen.draw()
            current_screen.handle_events()
            if (current_screen.choice == 'back'):
                print('back to main menu')
                current_screen = MainMenu(current_player)
            elif (current_screen.choice == 'math'):
                print("math was chosen")
                level = Level(1, 'math')
                current_screen = GameScreen('math', current_player, boss, level.getNextQuestion(), level.levelNum)
            elif (current_screen.choice == 'socialScience'):
                print("social science was chosen")
                level = Level(1, 'social_sciences')
                current_screen = GameScreen('socialScience', current_player, boss, level.getNextQuestion(), level.levelNum)
            elif (current_screen.choice == 'science'):
                print("science was chosen")
                level = Level(1, 'science')
                current_screen = GameScreen('science', current_player, boss, level.getNextQuestion(), level.levelNum)

        # math gameplay
        if (current_screen.type == 'math'):
            current_screen.display(screen)
            current_screen.handle_events()

            if (current_screen.answered):
                if (boss.bossHp <= 0) or (current_player.playerHP <= 0):
                    running = False
                elif (boss.bossHp <= 50 and boss.bossHp > 0):
                    level = Level(3, 'math')
                elif (boss.bossHp <= 80 and boss.bossHp > 50):
                    level = Level(2, 'math')
                elif (boss.bossHp <= 100 and boss.bossHp > 80):
                    level = Level(1, 'math')

                current_screen = GameScreen('math', current_player, boss, level.getNextQuestion(), level.levelNum)

        #science gameplay
        if (current_screen.type == 'science'):
            current_screen.display(screen)
            current_screen.handle_events()

            if (current_screen.answered):
                if (boss.bossHp <= 0) or (current_player.playerHP <= 0):
                    running = False
                elif (boss.bossHp <= 50 and boss.bossHp > 0):
                    level = Level(3, 'science')
                elif (boss.bossHp <= 80 and boss.bossHp > 50):
                    level = Level(2, 'science')
                elif (boss.bossHp <= 100 and boss.bossHp > 80):
                    level = Level(1, 'science')

                current_screen = GameScreen('science', current_player, boss, level.getNextQuestion(), level.levelNum)


        #social science gameplay
        if (current_screen.type == 'socialScience'):
            current_screen.display(screen)
            current_screen.handle_events()

            if (current_screen.answered):
                if (boss.bossHp <= 0) or (current_player.playerHP <= 0):
                    running = False
                elif (boss.bossHp <= 50 and boss.bossHp > 0):
                    level = Level(3, 'social_sciences')
                elif (boss.bossHp <= 80 and boss.bossHp > 50):
                    level = Level(2, 'social_sciences')
                elif (boss.bossHp <= 100 and boss.bossHp > 80):
                    level = Level(1, 'social_sciences')

                current_screen = GameScreen('science', current_player, boss, level.getNextQuestion(), level.levelNum)
                
                
        pygame.display.flip()
        
if __name__ == "__main__":
    run_game()