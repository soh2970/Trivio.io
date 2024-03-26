import pygame
import sys
import os
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons

class CorrectAnswerScreen(ScreenBase):

    def __init__(self, level):
        super().__init__()
        self.level = level
        self.image = pygame.image.load('images/correctAnswer.png')
        self.header = "You got it CORRECT!"
        if (level == 1): self.footer = "- 4 HP to BOSS"
        elif (level == 2): self.footer = "- 6 HP to BOSS"
        elif (level == 3): self.footer = "- 10 HP to BOSS"
        else: self.footer = "unknown level"

        self.continueButton = GameScreenButtons(self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 + 200, 130, 40, "Continue", lambda: self.choiceMade())
        self.nextQuestion = False

    def choiceMade(self):
        self.nextQuestion = True

    def draw(self):
        super().draw()

        #draw image onto screen
        image_resized = pygame.transform.scale(self.image, (200,200))
        self.screen.blit(image_resized, (self.screen.get_width()/2 - 95, self.screen.get_height()/2 - 230))
        
        #draw header text onto screen
        text_surface = self.MEDIUM_FONT.render(self.header, True, self.BLACK)
        self.screen.blit(text_surface, (self.screen.get_width()/2 - 230, self.screen.get_height()/2 + 40))

        #draw footer text onto screen
        text_surface = self.SMALLER_FONT.render(self.footer, True, self.RED)
        self.screen.blit(text_surface, (self.screen.get_width()/2 - 65, self.screen.get_height()/2 + 130))

        #draw continue button
        self.continueButton.draw(self.screen)

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
                self.continueButton.rect = pygame.Rect(self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 + 200, 130, 40)
            
            self.continueButton.handle_event(event)




