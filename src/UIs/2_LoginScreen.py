from screen import ScreenBase
import pygame
import sys
import os

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)
# initializing the constructor 
pygame.init() 

class LoginScreen(ScreenBase):

    def __init__(self):
        super().__init__()
        self.user_text=''
        self.pass_text=''

    def draw(self):
        super().draw()
        # get the current width and height of the screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        #rectangle
        username_rect= pygame.Rect(400, 250, 200, 32)
        password_rect= pygame.Rect(400, 300, 200, 32)

        username=self.SMALLER_FONT.render('Username:' , True , self.BLACK)
        password=self.SMALLER_FONT.render('Password:' , True , self.BLACK)
        login = self.MEDIUM_FONT.render('Log in to' , True , self.BLACK) 
        started = self.MEDIUM_FONT.render('get STARTED' , True , self.BLACK) 
        esc = self.PARAGRAPH_FONT.render('x' , True , self.BLACK) 
        ok = self.SMALLER_FONT.render('OK' , True , self.BLACK) 
        debug_mode = self.MODE_FONT.render('Debugger mode' , True , self.BLACK) 
        instruct_mode = self.MODE_FONT.render('Instructor mode' , True , self.BLACK) 

        #draw rectangle for usernamse input
        pygame.draw.rect(self.screen, self.GREY, username_rect)
        username_surface = self.BASE_FONT.render(self.user_text, True, (0, 0, 0))
        self.screen.blit(username_surface, (username_rect.x+5, username_rect.y+5))
        
        #draw rectangle for usernamse input
        pygame.draw.rect(self.screen, self.GREY, password_rect)
        password_surface = self.BASE_FONT.render(self.pass_text, True, (0, 0, 0))
        self.screen.blit(password_surface, (password_rect.x+5, password_rect.y+5))

        #button
        pygame.draw.rect(self.screen,self.BLUE,[self.width/2+100,self.height/2+50,45,30]) 
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-405,self.height/2-293,30,30]) 
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-350,self.height/2-290,90,20]) 
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-350,self.height/2-265,90,20]) 


        # superimposing the text onto our button 
        self.screen.blit(login, (self.width/2-200,self.height/2-200))
        self.screen.blit(started, (self.width/2-50,self.height/2-150))
        self.screen.blit(esc , (self.width/2-400,self.height/2-300)) 
        self.screen.blit(username, (150, 245))
        self.screen.blit(password, (165, 290))
        self.screen.blit(ok, (self.width/2+105, self.height/2+55))
        self.screen.blit(debug_mode, (self.width/2-349, self.height/2-285))
        self.screen.blit(instruct_mode, (self.width/2-348, self.height/2-260))




    def handle_events(self):
        # stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.running = False
                pygame.quit()
                sys.exit()
            # user resizing screen
            elif event.type == pygame.VIDEORESIZE:
                super().resize_screen()

            #checks if a mouse is clicked 
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                #if the mouse is clicked on the x button the game is terminated 
                if self.width/2-405 <= mouse[0] <= self.width/2-385 and self.height/2-293 <= mouse[1] <= self.height/2-263: 
                    pygame.quit() 
                if self.width/2+100 <= mouse[0] <= self.width/2+145 and self.height/2+50 <= mouse[1] <= self.height/2+80: 
                    print (self.user_text)
                    print (self.pass_text)
                    sys.exit() 
                    
                    
            elif event.type == pygame.KEYDOWN:
                #username
                if self.width/2-22 <= mouse[0] <= self.width/2+178 and self.height/2-50 <= mouse[1] <= self.height/2-18:
                    #check for backspace
                    if event.key == pygame.K_BACKSPACE:
                        #get text input
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text += event.unicode
                #password
                if self.width/2-22 <= mouse[0] <= self.width/2+178 and self.height/2 <= mouse[1] <= self.height/2+32:
                    if event.key == pygame.K_BACKSPACE:
                        #get text input
                        self.pass_text = self.pass_text[:-1]
                    else:
                        self.pass_text += event.unicode



    def run(self):
        super().run()

#initialize instance and run
if __name__ == '__main__':
    game_screen1 = LoginScreen()
    game_screen1.run()
