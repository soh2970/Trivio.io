import pygame
from src.UIs.screen import ScreenBase
from src.UIs.GameScreen2 import GameScreen
from question2 import Question
from Level import Level
from Player import Player
from Boss import Boss
from game import Game
from MainMenu import MainMenu


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
        
        current_screen.display(screen)
        current_screen.handle_events()

        pygame.display.flip()

        # if (current_screen.answered):
        #     if (boss.bossHp <= 0) or (player.playerHP <= 0):
        #         running = False
        #     elif (boss.bossHp <= 50 and boss.bossHp > 0):
        #         level = Level(3, category)
        #     elif (boss.bossHp <= 80 and boss.bossHp > 50):
        #         level = Level(2, category)
        #     elif (boss.bossHp <= 100 and boss.bossHp > 80):
        #         level = Level(1, category)

        #     current_screen = GameScreen(category, player, boss, level.getNextQuestion(), level.levelNum)

        
if __name__ == "__main__":
    run_game()
