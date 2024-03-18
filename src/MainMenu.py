import pygame
import sys
from game import Game

class MainMenu:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.font = pygame.font.Font('Corbel', 48)
        self.menu_items = ["Start New Game", "Load Game", "Exit"]
        self.selected_item = 0

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Main Menu")

    def run(self):
        while True:
            self.screen.fill(self.bg_color)
            self.draw_menu()
            self.check_events()
            pygame.display.flip()

    def draw_menu(self):
        for index, item in enumerate(self.menu_items):
            text_render = self.font.render(item, True, (0, 0, 0))
            text_rect = text_render.get_rect()
            text_rect.center = (self.screen_width // 2, 200 + index * 100)
            self.screen.blit(text_render, text_rect)

            if index == self.selected_item:
                pygame.draw.rect(self.screen, (255, 0, 0), text_rect, 2)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_item = (self.selected_item - 1) % len(self.menu_items)
                elif event.key == pygame.K_DOWN:
                    self.selected_item = (self.selected_item + 1) % len(self.menu_items)
                elif event.key == pygame.K_RETURN:
                    self.handle_selection()

    def handle_selection(self):
        if self.selected_item == 0:
            print("Start New Game selected")
            game = Game()
            game.startGame()
        elif self.selected_item == 1:
            print("Load Game selected")
            # Implement the logic to load a saved game
        elif self.selected_item == 2:
            print("Exit selected")
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.run()
