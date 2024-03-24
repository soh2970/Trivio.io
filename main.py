import pygame
from src.UIs.screen import ScreenBase
from src.UIs.GameScreen2 import GameScreen
from question2 import Question
from Level import Level


def run_game():
    screen = pygame.display.set_mode((844,600), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    level = Level(3, "math")
    
    current_screen = GameScreen('math', 'nate', level.getNextQuestion(), level.levelNum)
    
    while True:
        
        current_screen.handle_events()
        current_screen.display(screen)
        
        pygame.display.flip()
        


if __name__ == "__main__":
    run_game()
