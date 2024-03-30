import sys
import os
import pygame
from GameScreenButtons import GameScreenButtons
from screen import ScreenBase

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)


class InstructorPasswordScreen(ScreenBase):
    """
    
    """

    def __init__(self):
        super().__init__()
        self.password_text = ''
        self.active = False

    def draw(self):
        super().draw()
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        password_rect = pygame.Rect(400,300,200,32)

        titleOne = self.MEDIUM_FONT.render('Instructor', True, self.BLACK)
        titleTwo = self.MEDIUM_FONT.render('Password', True, self.BLACK)
        ok = self.SMALLER_FONT.render('OK', True, self.BLACK)
        cancel = self.SMALLER_FONT.render('Cancel', True, self.BLACK)
        esc = self.PARAGRAPH_FONT.render('x' , True , self.BLACK)

        pygame.draw.rect(self.screen, self.GREY, password_rect)
        passwordSurface = self.BASE_FONT.render(self.password_text, True, (0,0,0))
        self.screen.blit(passwordSurface, (password_rect.x+5, password_rect.y+5))

        pygame.draw.rect(self.screen,self.BLUE,[self.width/2+100,self.height/2+50,45,30]) 
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-405,self.height/2-293,30,30]) 
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-350,self.height/2-290,90,20]) 

        self.screen.blit(titleOne, (self.width/2-200, self.height/2-200))
        self.screen.blit(titleTwo, ((self.width/2-50,self.height/2-150)))
        self.screen.blit(ok, (self.width/2+105, self.height/2+55))
        self.screen.blit(cancel, (self.width/2-349, self.height/2-285))
        self.screen.blit(esc , (self.width/2-400,self.height/2-300))


    def check_password(self):
        if self.password_text == 'instruct':
            print("Password correct, entering instructor mode...")
            
        else:
            print("Instructor credential invalid.")

    def cancel(self):
        print("Cancelled")
        self.running = False


    def handle_events(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                super().resize_screen(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.width/2+100 <= mouse[0] <= self.width/2+145 and self.height/2+50 <= mouse[1] <= self.height/2+80:
                    self.check_password()
                    
                if self.width/2-405 <= mouse[0] <= self.width/2-385 and self.height/2-293 <= mouse[1] <= self.height/2-263:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_BACKSPACE:
                    self.password_text = self.password_text[:-1]
                else:
                    self.password_text += event.unicode


    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()

if __name__ == "__main__":
    InstructorPasswordScreen().run()