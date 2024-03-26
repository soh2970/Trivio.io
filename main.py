import pygame
from src.UIs.screen import ScreenBase
from src.UIs.GameScreen2 import GameScreen
from src.question2 import Question
from src.Level import Level
from src.Player import Player
from src.Boss import Boss
from src.game import Game
from src.MainMenu import MainMenu
from src.UIs.GameModeSelectScreen import GameModeSelectScreen


def run_game():

    running = True
    screen = pygame.display.set_mode((844,600), pygame.RESIZABLE)
    clock = pygame.time.Clock()



    category = "math"
    level = Level(1, category)
    player = Player('natetyu', 100, 0, 1)
    boss = Boss()
    current_screen = MainMenu("test")

    # GameScreen('math', player, boss, level.getNextQuestion(), level.levelNum)
    # newGame = Game()

    while running:

        if (current_screen.type == "mainMenu"):
            current_screen.display(screen)
            if (current_screen.handle_events() == 0):
                print("transitioning to category select screen")
                current_screen = GameModeSelectScreen()
                
        if (current_screen.type == 'gameModeSelect'):
            current_screen.draw()
            current_screen.handle_events()
            if (current_screen.choice == 'back'):
                print('successful test')
                current_screen = MainMenu('test')
            elif (current_screen.choice == 'math'):
                print("math was chosen")
                current_screen = GameScreen('math', player, boss, level.getNextQuestion(), level.levelNum)


        if (current_screen.type == 'math'):
            current_screen.display(screen)
            current_screen.handle_events()

            if (current_screen.answered):
                if (boss.bossHp <= 0) or (player.playerHP <= 0):
                    running = False
                elif (boss.bossHp <= 50 and boss.bossHp > 0):
                    level = Level(3, category)
                elif (boss.bossHp <= 80 and boss.bossHp > 50):
                    level = Level(2, category)
                elif (boss.bossHp <= 100 and boss.bossHp > 80):
                    level = Level(1, category)

                current_screen = GameScreen(category, player, boss, level.getNextQuestion(), level.levelNum)
                
        pygame.display.flip()
        
if __name__ == "__main__":
    run_game()