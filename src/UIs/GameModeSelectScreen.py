from src.UIs.screen import ScreenBase
import pygame
import sys
import os
from src.UIs.GameScreenButtons import GameScreenButtons

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)

pygame.init() 

class GameModeSelectScreen(ScreenBase):
    """
    Displays a screen for selecting the game mode within a Pygame application, offering
    users choices between different educational categories such as Math, Social Science,
    and Science. It facilitates the transition to game mode-specific screens based on the
    user's selection, while also providing options to navigate back or access tutorial content.

    Inherits from ScreenBase, using its window/screen setup capabilities to create a
    user-friendly selection interface.

    Attributes:
        clock (pygame.time.Clock): Manages screen update intervals to ensure smooth rendering.
        buttons (list of GameScreenButtons): Contains button objects for each game mode option,
            including actions for navigating to other screens.
        type (str): Screen identifier, used to differentiate this screen within the application.
        choice (str or None): Stores the user's selection. A specific category name for
            navigation to the respective game mode, 'back' for returning to the previous screen,
            or 'tutorial' for accessing the tutorial content.

    Methods:
        choiceMade(self, event): Captures and records the user's selection based on button interactions.
        draw(self): Renders the screen's graphical elements, including mode selection buttons and labels.
        handle_events(self): Listens for and processes user input events such as button clicks.
        run(self): Implements the main loop for the screen, continuously handling events and updating
            the screen's display to reflect the current state.

    The GameModeSelectScreen class encapsulates the functionality required for presenting users with
    a straightforward mode selection interface, enhancing the application's usability and navigation.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        self.clock = pygame.time.Clock()
        self.buttons = [
        GameScreenButtons(560, 280, 270, 90, "Math", lambda: self.choiceMade('math'), self.WHITE, self.BLACK ),
        GameScreenButtons(290, 280, 270, 90, "Social Science", lambda: self.choiceMade('social_sciences'), self.WHITE, self.BLACK ),
        GameScreenButtons(20, 280, 270, 90, "Science", lambda: self.choiceMade('science'), self.WHITE, self.BLACK ),
        GameScreenButtons(30, 70, 70, 50, "Back", lambda: self.choiceMade('back'), self.WHITE, self.BLACK ),
        GameScreenButtons(700, 380, 100, 60, "Tutorial", lambda: self.choiceMade('tutorial'), self.WHITE, self.BLACK ),
        ]
        self.type = 'gameModeSelect'
        self.choice = None



    def choiceMade(self, event):
        self.choice = event
        

    def draw(self):
        super().draw()
        # get the current width and height of the screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        #back to main menu button
        back = self.BUTTON_FONT.render('Back' , True , 0) 
        #start tutorial button
        start = self.BUTTON_FONT.render('Start Tutorial >>', True, 0)
        #texts on screen
        mode = self.PARAGRAPH_FONT.render('Mode Selection', True, 0)
        categories = self.SMALLER_FONT.render('Select a Category to start', True, 0)
        category_text = self.SMALLER_FONT.render('Category', True, 0)
        
        for button in self.buttons:
            button.draw(self.screen)
        # self.radioButtons = [
        #     RadioButton(560, 280, 270, 60, self.PARAGRAPH_FONT, "Math"),
        #     RadioButton(290, 280, 270, 60, self.PARAGRAPH_FONT, "Social Science"),
        #     RadioButton(20, 280, 270, 60, self.PARAGRAPH_FONT, "Science")
        # ]
        # self.group = pygame.sprite.Group(self.radioButtons)
        
        # self.group.draw(self.screen)


        # #back button display
        # pygame.draw.rect(self.screen,self.GREY,[self.width/2-400,self.height/2-293,60,30]) 
        # self.screen.blit(back , (self.width/2-397,self.height/2-290)) 


        self.screen.blit(categories, (self.width/2-140,self.height/2-180))
        self.screen.blit(mode, (self.width/2-130, self.height/2-230))
        self.screen.blit(category_text, (self.width/2-370, self.height/2-60))

        # #start tutorial button
        # pygame.draw.rect(self.screen,self.BLUE,[self.width/2+215,self.height/2+50,180,40]) 
        # self.screen.blit(start, (self.width/2+220,self.height/2+60))

        


    def handle_events(self):
        self.clock.tick(60)
        mouse = pygame.mouse.get_pos()

        # for rb in self.radioButtons:
        #     rb.setRadioButtons(self.radioButtons)
        # self.radioButtons[0].clicked = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            for button in self.buttons:
                button.handle_event(event)
            """
            need to be changed
            """

            # if event.type == pygame.MOUSEBUTTONDOWN: 
            #     if self.width/2-400 <= mouse[0] <= self.width /2-340 and self.height/2-293 <= self.mouse[1] <= self.height/2-263: 
            #         pygame.quit() #CHANGE to previous screen New/Save mode
            #     if self.width/2+215 <= mouse[0] <= self.width /2+395 and self.height/2+50 <= self.mouse[1] <= self.height/2+90: 
            #         pygame.quit() #CHANGE to next tutorial screen 
            # user resizing screen
            if event.type == pygame.VIDEORESIZE:
                super().resize_screen(event)

        # self.group.update(event_list)

    def run(self):
        super().run()

class RadioButton(pygame.sprite.Sprite):
    """
    A RadioButton is a visual element that can be selected or deselected.

    Attributes:
        button_image (pygame.Surface): The default image of the button when not interacted with.
        hover_image (pygame.Surface): The image of the button when the mouse hovers over it.
        clicked_image (pygame.Surface): The image of the button when it has been clicked and selected.
        image (pygame.Surface): The current image of the button being displayed.
        rect (pygame.Rect): The rectangle area that the button covers.
        clicked (bool): Indicates whether the button is currently selected.
        buttons (list): A list of other radio button instances that this button is grouped with.

    Methods:
        setRadioButtons(buttons): Associates this radio button with a group of other radio buttons.
        update(event_list): Updates the button's state based on the provided events.
    """
    def __init__(self, x, y, w, h, font, text):
        super().__init__() 
        text_surf = font.render(text, True, (0, 0, 0))
        self.button_image = pygame.Surface((w, h))
        self.button_image.fill((228, 246, 248))
        self.button_image.blit(text_surf, text_surf.get_rect(center = (w // 2, h // 2)))
        self.hover_image = pygame.Surface((w, h))
        self.hover_image.fill((228, 246, 248))
        self.hover_image.blit(text_surf, text_surf.get_rect(center = (w // 2, h // 2)))
        pygame.draw.rect(self.hover_image, (0,71,100), self.hover_image.get_rect(), 5)
        self.clicked_image = pygame.Surface((w, h))
        self.clicked_image.fill((135,206,250))
        self.clicked_image.blit(text_surf, text_surf.get_rect(center = (w // 2, h // 2)))
        self.image = self.button_image
        self.rect = pygame.Rect(x, y, w, h)
        self.clicked = False
        self.buttons = None

    def setRadioButtons(self, buttons):
        self.buttons = buttons

    def update(self, event_list):
        hover = self.rect.collidepoint(pygame.mouse.get_pos())
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover and event.button == 1:
                    for rb in self.buttons:
                        rb.clicked = False
                        print('clicked')
                    self.clicked = True
        
        self.image = self.button_image
        if self.clicked:
            self.image = self.clicked_image
        elif hover:
            self.image = self.hover_image



#initialize instance and run
if __name__ == '__main__':
    game_screen1 = GameModeSelectScreen()
    game_screen1.run()