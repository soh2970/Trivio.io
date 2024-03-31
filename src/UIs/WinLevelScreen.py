import pygame
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons
import sys

class WinLevelScreen(ScreenBase):
    def __init__(self, next_level_callback=None):
        super().__init__()
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.setup_buttons()
        self.setup_texts()
        self.nextLevel = True
        self.next_level_callback = next_level_callback
        button_color = self.BLUE
        text_color = self.BLACK
        next_level_button_pos = (self.width/5*4, self.height/15*13, 80, 30)
        self.next_level_button = GameScreenButtons(*next_level_button_pos, "Next Level", self.on_next_level, button_color, text_color)


    def on_next_level(self):
            print("Next Level")
            self.nextLevel = True
            if self.next_level_callback:
                self.next_level_callback()

    def on_save_game(self):
            print("Game Saved")

    def on_options(self):
            print("Options")



    def setup_buttons(self):
        # Button callbacks

        # Button positions and sizes
        save_game_button_pos = (self.width/5*4, self.height/15*1, 80, 30)
        options_button_pos = (self.width/5*4, self.height/15*2, 80, 30)

        # Button colors
        button_color = self.BLUE
        text_color = self.BLACK

        # Creating button instances
        self.save_game_button = GameScreenButtons(*save_game_button_pos, "Save Game", self.on_save_game, button_color, text_color)
        self.options_button = GameScreenButtons(*options_button_pos, "Options", self.on_options, button_color, text_color)

    def setup_texts(self):
        # Heading texts
        self.text1 = self.HEADING_FONT.render('LEVEL', True, self.BLACK)
        self.textRect1 = self.text1.get_rect(center=(self.width//2, self.height/12*5))
        self.text2 = self.HEADING_FONT.render('PASSED', True, self.BLACK)
        self.textRect2 = self.text2.get_rect(center=(self.width//2, self.height/12*7))

    def draw(self):
        super().draw()
        # Draw headings
        self.screen.blit(self.text1, self.textRect1)
        self.screen.blit(self.text2, self.textRect2)
        # Draw buttons
        self.next_level_button.draw(self.screen)
        self.save_game_button.draw(self.screen)
        self.options_button.draw(self.screen)

    def handle_events(self):

        event_list = pygame.event.get()
        for event in event_list:

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                self.next_level_button.handle_event(event)
                self.save_game_button.handle_event(event)
                self.options_button.handle_event(event)

if __name__ == "__main__":
    pygame.init()
    game_screen = WinLevelScreen()
    game_screen.run()
