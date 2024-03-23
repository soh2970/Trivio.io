import pygame
from src.UIs.screen import ScreenBase
from src.UIs.GameScreen2 import GameScreen
from question2 import Question


def run_game():
    screen = pygame.display.set_mode((844,600), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    
    q = Question(1, "What is the perimeter of a rectangle with diagonal length 17 units and length 8 units?", ["1","2","3","4"], "2", 4, False, "Math")
    current_screen = GameScreen('math', 'nate', q)
    
    while True:
        
        current_screen.process_events()
        current_screen.display(screen)
        
        pygame.display.flip()
        

if __name__ == "__main__":
    run_game()
