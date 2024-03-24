"""
Win Game Screen

"""
from screen import ScreenBase
import pygame

class WinGameScreen(ScreenBase):

    def __init__(self):
        super().__init__()
        # get the current width and height of the screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

    def draw(self):
        super().draw()
        self.text = self.PARAGRAPH_FONT.render('START' , True , self.BLACK) 
        self.welcome = self.MEDIUM_FONT.render('WELCOME TO' , True , self.BLACK) 
        self.trivio = self.MEDIUM_FONT.render('T R I V I O' , True , self.BLACK) 
        self.esc = self.PARAGRAPH_FONT.render('x' , True , self.BLACK) 
        
		#button
        pygame.draw.rect(self.screen,self.BLUE,[self.width/2-100,self.height/2+100,200,40]) 
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-405,self.height/2-293,30,30]) 

		# superimposing the text onto our button 
        self.screen.blit(self.text , (self.width/2-65,self.height/2+100))
        self.screen.blit(self.welcome, (self.width/2-200,self.height/2-100))
        self.screen.blit(self.trivio, (self.width/2,self.height/2))
        self.screen.blit(self.esc , (self.width/2-400,self.height/2-300))

    def handle_events(self):
        # call parent class event handling
        super().handle_events()
		# stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos() 
        for event in pygame.event.get():
              if ev.type == pygame.MOUSEBUTTONDOWN: 
                        #if the mouse is clicked on the x button the game is terminated 
                                   if self.width/2-405 <= mouse[0] <= self.width/2+435 and self.height/2-293 <= mouse[1] <= self.height/2-263: 
                                           pygame.quit() 
                                           
										   
    def run(self):
        super().run()

#initialize instance and run
if __name__ == '__main__':
    game_screen1 = WinGameScreen()
    game_screen1.run()
