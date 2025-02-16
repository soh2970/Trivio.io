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
    """
    A screen for user login in a Pygame application, providing fields for username and password input,
    as well as buttons for submitting the login request or creating a new account.

    Attributes:
        user_text (str): Text input by the user for the username.
        pass_text (str): Text input by the user for the password.
        usernameInput (bool): Indicates if the username input box is active.
        passwordInput (bool): Indicates if the password input box is active.
        transitionToDebuggerPassword (bool): Flag to transition to the debugger password screen.
        transitionToInstructorPassword (bool): Flag to transition to the instructor password screen.
        type (str): Identifier for the screen type, set to 'loginScreen'.
        input_box (pygame.Rect): Rectangle for the username input box.
        pass_input_box (pygame.Rect): Rectangle for the password input box.
        input_box_color (pygame.Color): Color of the input boxes.
        text_color (tuple): Color of the input text.
        loginButton (GameScreenButtons): Button for logging in.
        createAccountButton (GameScreenButtons): Button for creating a new account.
        isValidUser (bool): Indicates whether the user is validated.
        Player (Player or None): The player instance created upon successful login.

    Methods:
        handleLogIn(self):
            Handles the login logic, validating the user credentials.

        handleCreateAccount(self):
            Handles the creation of a new user account.

        draw(self):
            Renders the login screen, including input fields and buttons.

        handle_events(self):
            Handles events such as text input, button clicks, and transitions.

        run(self):
            Contains the main loop for the LoginScreen, handling events and rendering updates.
    """
    def __init__(self, current_width, current_height):
        super().__init__(current_width, current_height)
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
        self.input_box = pygame.Rect(self.screen_width/211*78, self.screen_height/120*57, 200, 40)  # Position and size of the input box
        self.text_color = self.BLACK
        self.font = self.SMALLER_FONT
        self.active = False  # Indicates if the input box is active

        # password input box setup
        self.pass_input_box_color = pygame.Color('dodgerblue2')
        self.pass_input_box = pygame.Rect(self.screen_width/211*78, self.screen_height/20*11, 200, 40)  # Position and size of the input box
        self.pass_text_color = self.BLACK
        self.font = self.SMALLER_FONT
        self.pass_active = False  # Indicates if the input box is active

        self.loginButton = GameScreenButtons(self.screen_width/211*68, self.screen_height/3*2, 100, 30, "Log In", lambda: self.handleLogIn(), self.WHITE, self.BLACK)
        self.createAccountButton = GameScreenButtons(self.screen_width/211*103, self.screen_height/3*2, 200, 30, "Create Account", lambda: self.handleCreateAccount(), self.WHITE, self.BLACK)
        self.isValidUser = False
        self.Player = None

        self.userFoundError = False
        self.loginError = False

    def handleLogIn(self):
        user = UserAccount(self.user_text, self.pass_text)
        if (user.validateLogin() == True):
            self.isValidUser = True
            player = Player(user.ID, 100, 0, 1)
            self.Player = player
        elif (user.validateLogin() == False):
            print("incorrect username or password")
            self.loginError = True

    def handleCreateAccount(self):
        print("account created")
        user = UserAccount(self.user_text, self.pass_text)
        try:
            user.createAccount()
            self.isValidUser = True
            player = Player(user.ID, 100, 0, 1)
            self.Player = player
        except: 
            print("user already in account")
            self.userFoundError = True

            


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
        pygame.draw.rect(self.screen,self.GREY,[self.screen_width/844*17,self.screen_height/600*7,30,30]) 
        pygame.draw.rect(self.screen, self.GREY, [self.screen_width/211*18, self.screen_height/60, 90, 20])

        pygame.draw.rect(self.screen,self.GREY,[self.screen_width/844*72,self.screen_height/600*35,90,20]) 


        # superimposing the text onto our button 
        self.screen.blit(login, (self.screen_width/844*222,self.screen_height/6))
        self.screen.blit(started, (self.screen_width/844*372,self.screen_height/60*15))
        self.screen.blit(esc , (self.screen_width/422*11,0)) 
        self.screen.blit(username, (self.screen_width/844*172, self.screen_height/60*29))
        self.screen.blit(password, (self.screen_width/844*172, self.screen_height/60*34))
        self.screen.blit(debug_mode, (self.screen_width/844*73, self.screen_height/40))
        self.screen.blit(instruct_mode, (self.screen_width/844*74, self.screen_height/15))

        
       
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

        if (self.userFoundError == True):
            txt_surface = self.font.render("User already in database", True, self.RED)
            self.screen.blit(txt_surface, (self.screen_width/25*8, self.screen_height/25*20))

        if (self.loginError == True):
            txt_surface = self.font.render("Invalid Login Information", True, self.RED)
            self.screen.blit(txt_surface, (self.screen_width/25*8, self.screen_height/25*20 + 40))


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
                self.input_box = pygame.Rect(self.screen_width/844*312, self.screen_height/600*285, 200, 40)
                self.pass_input_box = pygame.Rect(self.screen_width/844*312, self.screen_height/20*11, 200, 40)
                self.loginButton.rect = pygame.Rect(self.screen_width/844*272, self.screen_height/3*2, 100, 30)
                self.createAccountButton.rect = pygame.Rect(self.screen_width/211*103, self.screen_height/3*2, 200, 30)

                self.loginButton = GameScreenButtons(self.screen_width/211*68, self.screen_height/3*2, 100, 30, "Log In", lambda: self.handleLogIn(), self.WHITE, self.BLACK)
                self.createAccountButton = GameScreenButtons(self.screen_width/211*103, self.screen_height/3*2, 200, 30, "Create Account", lambda: self.handleCreateAccount(), self.WHITE, self.BLACK)
            
            #checks if a mouse is clicked 
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Transition to DebuggerPasswordScreen
                if self.screen_width/211*18 <= mouse[0] <= self.screen_width/211*18+100 and self.screen_height/60 <= mouse[1] <= self.screen_height/60+14:
                    print("debugger clicked")
                    self.transitionToDebuggerPassword = True

                # Transition to InstructorPasswordScreen
                if self.screen_width/211*18 <= mouse[0] <= self.screen_width/211*18+100 and self.screen_height/24 <= mouse[1] <= self.screen_height/24+20:
                    print("instructor clicked")
                    self.transitionToInstructorPassword = True

                #if the mouse is clicked on the x button the game is terminated 
                if self.screen_width/844*17 <= mouse[0] <= self.screen_width/844*17+20 and self.screen_height/600*7 <= mouse[1] <= self.screen_height/600*7+30: 
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
