from screen import ScreenBase
import pygame
import sys
import os

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)
# initializing the constructor 
pygame.init() 

class InstructorPassScreen(ScreenBase):

    def __init__(self):
        super().__init__()
        # screen width and height
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

    def draw(self):
        super().draw()

        # text for buttons
        self.text_new_game = self.SMALLER_FONT.render('New Game', True, self.BLACK)
        self.text_saved_game = self.SMALLER_FONT.render('Saved Game', True, self.BLACK)
        self.text_esc = self.PARAGRAPH_FONT.render('x', True, self.BLACK)
        self.text_or = self.PARAGRAPH_FONT.render('OR',True, self.BLACK )

        # draw the buttons
        pygame.draw.circle(self.screen, self.GREEN, (self.width/4, self.height/2), 100)
        pygame.draw.circle(self.screen, self.BLUE, (3*self.width/4, self.height/2), 100)

        # put the text on the buttons
        self.screen.blit(self.text_new_game, (self.width/4 - self.text_new_game.get_width()/2, self.height/2 - self.text_new_game.get_height()/2))
        self.screen.blit(self.text_saved_game, (3*self.width/4 - self.text_saved_game.get_width()/2, self.height/2 - self.text_saved_game.get_height()/2))

        # draw close button
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-405,self.height/2-293,30,30]) 
        self.screen.blit(self.text_esc , (self.width/2-400,self.height/2-300)) 

        #put or on the screen
        self.screen.blit(self.text_or, (self.width/2-25, self.height/2-10))

    def handle_events(self):
        # stores the (x,y) coordinates into the variable as a tuple
        self.mouse = pygame.mouse.get_pos() 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            # user resizing screen
            elif event.type == pygame.VIDEORESIZE:
                super().resize_screen()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                mouse = pygame.mouse.get_pos()

                # close button (top left corner)
                if self.width/2-405 <= mouse[0] <= self.width/2-385 and self.height/2-293 <= mouse[1] <= self.height/2-263: 
                    pygame.quit() 

                """
                needs the new handling events for new game or saved game - game script? 
                """

    def run(self):
        super().run()

#initialize instance and run
if __name__ == '__main__':
    game_screen1 = InstructorPassScreen()
    game_screen1.run()
