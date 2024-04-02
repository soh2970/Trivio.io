import pygame
import sys
from src.UIs.screen import ScreenBase

class MainMenu(ScreenBase):
    """
    Represents the main menu of a Pygame application, where a player can choose to start a new game,
    load an existing game, or exit the application. This class inherits from ScreenBase, using its
    setup for the Pygame window/screen along with additional functionalities specific to the main menu.

    Attributes:
        player (Player): The player instance associated with the main menu.
        screen_width (int): The width of the screen.
        screen_height (int): The height of the screen.
        bg_color (tuple): The background color of the menu.
        font (pygame.font.Font): The font used for menu item texts.
        menu_items (list): A list of strings representing the menu options available.
        selected_item (int): The index of the currently selected menu item.
        running (bool): A flag to control the main loop, indicating if the menu is currently active.
        type (str): A string identifier for the screen type, set to 'mainMenu'.

    Methods:
        run(self):
            Contains the main loop for the MainMenu, processing events and updating the display.

        display(self, screen):
            Renders the main menu options on the provided Pygame screen object. Highlights the currently selected menu item and displays the logged-in user.

        handle_events(self):
            Processes input events such as navigation through menu items and selection.

        handle_selection(self):
            Executes the action associated with the selected menu item, such as starting a new game, loading a game, or exiting.
    """
    def __init__(self, player):
        super().__init__()
        self.screen_width = 844
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.font = pygame.font.SysFont('Corbel', 48)
        self.menu_items = ["Start New Game", "Load Game", "Exit"]
        self.selected_item = 0
        self.running = False  # Flag to control the main loop
        self.player = player
        self.type = "mainMenu"

    def run(self):
        self.running = True
        while self.running:

            self.check_events()
            pygame.display.flip()

    def display(self, screen):
        
        #display which user is currently logged in
        screen.fill(self.bg_color)
        userText = f'Logged in as {self.player.playerId}'
        text_render = self.font.render(userText, True, (0, 0, 0))
        text_rect = text_render.get_rect()
        text_rect.center = (self.screen_width // 2, 200)
        screen.blit(text_render, (self.screen_width/2 - 300, self.screen_height/2 - 250))       

        
        for index, item in enumerate(self.menu_items):
            text_render = self.font.render(item, True, (0, 0, 0))
            text_rect = text_render.get_rect()
            text_rect.center = (self.screen_width // 2, 200 + index * 100)
            screen.blit(text_render, text_rect)

            if index == self.selected_item:
                pygame.draw.rect(screen, (255, 0, 0), text_rect, 2)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # Exit the main loop
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_item = (self.selected_item - 1) % len(self.menu_items)
                elif event.key == pygame.K_DOWN:
                    self.selected_item = (self.selected_item + 1) % len(self.menu_items)
                elif event.key == pygame.K_RETURN:
                    return self.handle_selection()

    def handle_selection(self):
        if self.selected_item == 0:
            print("Start New Game selected")
            # self.game_instance.startGame()
            # self.running = False
            return 0
        elif self.selected_item == 1:
            print("Load Game selected")
            # Implement the logic to load a saved game
        elif self.selected_item == 2:
            print("Exit selected")
            self.running = False  # Exit the main loop
            pygame.quit()
            sys.exit()

