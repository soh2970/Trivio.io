from src.UIs.screen import ScreenBase
import pygame
import sys
import os
from src.UIs.GameScreenButtons import GameScreenButtons
from src.UserAccount import UserAccount
from src.Player import Player
from src.UIs.DebuggerPasswordScreen import DebuggerPasswordScreen
from src.UIs.InstructorPasswordScreen import InstructorPasswordScreen

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
        self.usernameInput = False
        self.passwordInput = False
        self.transitionToDebuggerPassword = False
        self.transitionToInstructorPassword = False
        self.type = 'loginScreen'
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        # username input box setup
        self.input_box_color = pygame.Color('dodgerblue2')
        self.input_box = pygame.Rect(self.screen.get_width()/2 - 110, self.screen.get_height()/2 - 15, 200, 40)  # Position and size of the input box
        self.text_color = self.BLACK
        self.font = self.SMALLER_FONT
        self.active = False  # Indicates if the input box is active

        # password input box setup
        self.pass_input_box_color = pygame.Color('dodgerblue2')
        self.pass_input_box = pygame.Rect(self.screen.get_width()/2 - 110, self.screen.get_height()/2 + 30, 200, 40)  # Position and size of the input box
        self.pass_text_color = self.BLACK
        self.font = self.SMALLER_FONT
        self.pass_active = False  # Indicates if the input box is active

        self.loginButton = GameScreenButtons(self.screen.get_width()/2 - 150, self.screen.get_height()/2 + 100, 100, 30, "Log In", lambda: self.handleLogIn(), self.WHITE, self.BLACK)
        self.createAccountButton = GameScreenButtons(self.screen.get_width()/2 - 10, self.screen.get_height()/2 + 100, 200, 30, "Create Account", lambda: self.handleCreateAccount(), self.WHITE, self.BLACK)
        self.isValidUser = False
        self.Player = None

    def handleLogIn(self):
        print("logged in")
        user = UserAccount(self.user_text, self.pass_text)
        if (user.validateLogin() == True):
            self.isValidUser = True
            player = Player(user.ID, 100, 0, 1)
            self.Player = player

    def handleCreateAccount(self):
        print("account created")
        user = UserAccount(self.user_text, self.pass_text)
        user.createAccount()
        self.isValidUser = True
        player = Player(user.ID, 100, 0, 1)
        self.Player = player

    def draw(self):
        super().draw()
        # get the current width and height of the screen


        username=self.SMALLER_FONT.render('Username:' , True , self.BLACK)
        password=self.SMALLER_FONT.render('Password:' , True , self.BLACK)
        login = self.MEDIUM_FONT.render('Log in to' , True , self.BLACK) 
        started = self.MEDIUM_FONT.render('get STARTED' , True , self.BLACK) 
        esc = self.PARAGRAPH_FONT.render('x' , True , self.BLACK) 
        ok = self.SMALLER_FONT.render('OK' , True , self.BLACK) 
        debug_mode = self.MODE_FONT.render('Debugger mode' , True , self.BLACK) 
        instruct_mode = self.MODE_FONT.render('Instructor mode' , True , self.BLACK) 

        #button
        pygame.draw.rect(self.screen,self.GREY,[self.width/2-405,self.height/2-293,30,30]) 
        pygame.draw.rect(self.screen, self.GREY, [self.width/2-350, self.height/2-290, 90, 20])

        pygame.draw.rect(self.screen,self.GREY,[self.width/2-350,self.height/2-265,90,20]) 


        # superimposing the text onto our button 
        self.screen.blit(login, (self.width/2-200,self.height/2-200))
        self.screen.blit(started, (self.width/2-50,self.height/2-150))
        self.screen.blit(esc , (self.width/2-400,self.height/2-300)) 
        self.screen.blit(username, (self.width/2 - 250, self.height/2 - 10))
        self.screen.blit(password, (self.width/2 - 250, self.height/2 + 40))
        self.screen.blit(debug_mode, (self.width/2-349, self.height/2-285))
        self.screen.blit(instruct_mode, (self.width/2-348, self.height/2-260))

        
       
        # Render the current username text.
        txt_surface = self.font.render(self.user_text, True, self.text_color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        self.input_box.w = width
        # Blit the text.
        self.screen.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(self.screen, self.input_box_color, self.input_box, 2)

        # Render the current password text.
        txt_surface = self.font.render(self.pass_text, True, self.text_color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        self.pass_input_box.w = width
        # Blit the text.
        self.screen.blit(txt_surface, (self.pass_input_box.x+5, self.pass_input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(self.screen, self.pass_input_box_color, self.pass_input_box, 2)


        #Render the create account and log in buttons
        self.loginButton.draw(self.screen)
        self.createAccountButton.draw(self.screen)


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
                super().resize_screen(event)

                #resizes buttons based on window size
                self.input_box = pygame.Rect(self.screen.get_width()/2 - 110, self.screen.get_height()/2 - 15, 200, 40)
                self.pass_input_box = pygame.Rect(self.screen.get_width()/2 - 110, self.screen.get_height()/2 + 30, 200, 40)
                self.loginButton.rect = pygame.Rect(self.screen.get_width()/2 - 150, self.screen.get_height()/2 + 100, 100, 30)
                self.createAccountButton.rect = pygame.Rect(self.screen.get_width()/2 - 10, self.screen.get_height()/2 + 100, 200, 30)
            
            #checks if a mouse is clicked 
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Transition to DebuggerPasswordScreen
                if self.width/2-350 <= mouse[0] <= self.width/2-250 and self.height/2-290 <= mouse[1] <= self.height/2-270:
                    print("debugger clicked")
                    self.transitionToDebuggerPassword = True

                # Transition to InstructorPasswordScreen
                if self.width/2-350 <= mouse[0] <= self.width/2-250 and self.height/2-275 <= mouse[1] <= self.height/2-255:
                    print("instructor clicked")
                    self.transitionToInstructorPassword = True

                #if the mouse is clicked on the x button the game is terminated 
                if self.width/2-405 <= mouse[0] <= self.width/2-385 and self.height/2-293 <= mouse[1] <= self.height/2-263: 
                    pygame.quit()


                # If the user clicked on the username input box rect.
                if self.input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.active = not self.active
                else:
                    self.active = False

                if self.pass_input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.pass_active = not self.pass_active
                else:
                    self.pass_active = False

            """
                Checks for user input
            """
            if event.type == pygame.KEYDOWN:

                """ user input for username"""
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print(self.user_text)
                        self.user_text = ''  # Reset text after enter
                    elif event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text += event.unicode

                """ user input for password """
                if self.pass_active:
                    if event.key == pygame.K_RETURN:
                        print(self.pass_text)
                        self.pass_text = ''  # Reset text after enter
                    elif event.key == pygame.K_BACKSPACE:
                        self.pass_text = self.pass_text[:-1]
                    else:
                        self.pass_text += event.unicode
                
            self.loginButton.handle_event(event)
            self.createAccountButton.handle_event(event)

    def run(self):
        super().run()

#initialize instance and run
if __name__ == '__main__':
    game_screen1 = LoginScreen()
    game_screen1.run()
