"""
Options Screen
gives players options to change aspects 
Add a reset button

"""
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons
from src.UIs.AudioManager import AudioManager
import pygame
import os
import sys

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)


class OptionsScreen(ScreenBase):

    def __init__(self, audio_manager, width, height):
        super().__init__(width, height)

        self.goBack = False
        self.audio_manager = audio_manager
        self.vol_slider = slider(self.screen.get_width()/5*2, self.screen.get_width()/5*4, self.screen.get_height()/12*7, self.screen.get_width()/5*3, self.audio_manager)
        self.type = "options"

    def draw(self):
        super().draw()

        # get the current width and height of the screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        #text
        self.text1 = self.MEDIUM_FONT.render('Options', True, self.BLACK)
        self.textRect1 = self.text1.get_rect(center = (self.width//2, self.height/12*3))
        self.volume_text = self.BUTTON_FONT.render('VOLUME', True, self.BLACK)
        self.vol_textrect = self.volume_text.get_rect(center = (self.width/5, self.height/12*7))
        #self.song_text = self.BUTTON_FONT.render('SONG', True, self.BLACK)
        #self.song_textrect = self.song_text.get_rect(center = (self.width/5, self.height/12*7))
        #self.brightness_text = self.BUTTON_FONT.render('DISPLAY', True, self.BLACK)
        #self.brightness_textrect = self.brightness_text.get_rect(center = (self.width/5, self.height/12*9))
        
        # slider
        pygame.draw.line(self.screen, self.BLACK, (self.vol_slider.x1, self.vol_slider.height), (self.vol_slider.x2, self.vol_slider.height), 3)
        # slider button
        pygame.draw.circle(self.screen, self.BLACK, (self.vol_slider.pos, self.vol_slider.height), 10)
        
        self.back_button = GameScreenButtons(self.width/25*1, self.height/25*1, 80,30, "Back", lambda: self.choiceMade(), self.GREY, self.BLACK)
        self.back_button.draw(self.screen)
 
        '''
        #back button 
        self.back_button = pygame.draw.rect(self.screen, self.BLACK, (self.width/25*1, self.height/25*1, 80,30),1)
        self.back_button_text = self.BUTTON_FONT.render("Back", (self.back_button.centerx, self.back_button.centery), self.BLACK)
        self.back_button_rect = self.back_button_text.get_rect(center = self.back_button.center)
        self.screen.blit(self.back_button_text, self.back_button_rect)
        '''
        '''
        #arrows
        self.leftArrow = ArrowButton(self.width/5*2, self.height/12*7, 50,50,'left')
        self.rightArrow = ArrowButton(self.width/5*4, self.height/12*7, 50, 50, 'right')

        #buttons
        
        self.light_button = pygame.draw.rect(self.screen, self.BLACK, (self.width/5*2, self.height/15*10.5, 160,60),1)
        self.light_button_text = self.SMALLER_FONT.render("Light", (self.light_button.centerx, self.light_button.centery), self.BLACK)
        self.light_button_textrect = self.light_button_text.get_rect(center = self.light_button.center)
        self.dark_button = pygame.draw.rect(self.screen, self.DARKGREY, (self.width/5*3, self.height/15*10.5, 160,60))
        self.dark_button_text = self.SMALLER_FONT.render("Dark", (self.dark_button.centerx, self.dark_button.centery), self.WHITE)
        self.dark_button_textrect = self.dark_button_text.get_rect(center = self.dark_button.center)
        back = self.BUTTON_FONT.render('Back' , True , 0) 
        '''
        # display text
        self.screen.blit(self.text1, self.textRect1)
        self.screen.blit(self.volume_text, self.vol_textrect)
        '''
        self.screen.blit(self.song_text, self.song_textrect)
        self.screen.blit(self.brightness_text, self.brightness_textrect)
        
        #display buttons
        self.screen.blit(self.light_button_text, self.light_button_textrect)
        self.screen.blit(self.dark_button_text, self.dark_button_textrect)
        '''
        #display arrows
        #left_arrow_image_path= ''
        #left_arrow_image = pygame.image.load(left_arrow_image_path)
        #left_arrow_image_resized = pygame.transform.scale(boss2_image, (80,80))
        #right_arrow_image_path = ''
        #right_arrrow_image = pygame.image.load(boss2_image_path)
        #right_arrow_image_resized = pygame.transform.scale(boss2_image, (80,80))
        '''
        self.screen.blit(self.leftArrow.image, self.leftArrow.rect)
        self.screen.blit(self.rightArrow.image, self.rightArrow.rect)
        '''     

    def handle_events(self):
        # stores the (x,y) coordinates into the variable as a tuple
        self.mouse = pygame.mouse.get_pos() 

        events = pygame.event.get()
        self.vol_slider.slider_events(events)

       # self.leftArrow.arrow_clicks(events)
       # self.rightArrow.arrow_clicks(events)

        for event in events:
            # user quits
            if event.type == pygame.QUIT: 
                self.running = False
                pygame.quit()
                sys.exit()
            # user resizing screen
            elif event.type == pygame.VIDEORESIZE:
                super().resize_screen(event)
                self.vol_slider.update_slider_pos(self.width,self.height)

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.back_button.handle_event(event)
    
    def choiceMade(self):
        print("user wants to go back")
        self.goBack = True
        
    
    def run(self):
        super().run()

class slider:
    def __init__(self, low, high, h, initial_pos, audio_manager):
        self.x1 = low # left slider x-coord
        self.x2 = high # right sldier x-coord
        self.height = h # slider y value
        self.pos = initial_pos
        self.colour = (0,0,0)
        self.is_dragging = False  # Track whether the slider is being dragged
        self.audio_manager = audio_manager
    
    def update_slider_pos(self, slider_width, slider_height):
        # Horizontal positions based on percentage of screen width
        self.x1 = slider_width * 0.35  # 25% from the left edge of the screen
        self.x2 = slider_width * 0.75  # 75% from the left edge of the screen
        
        # Vertical position based on percentage of screen height
        self.height = slider_height * 0.6  # 60% from the top of the screen

        # Update slider position (if you're tracking the knob's position as a percentage)
        self.pos = self.x1 + (self.volume * (self.x2 - self.x1))

    def slider_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if abs(event.pos[0] - self.pos) < 10 and abs(event.pos[1] - self.height) < 10:
                    self.is_dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.is_dragging = False
                self.adjust_volume()
            elif event.type == pygame.MOUSEMOTION and self.is_dragging:
                self.pos = min(max(event.pos[0], self.x1), self.x2)

    def adjust_volume(self):
        self.volume = (self.pos - self.x1) / (self.x2 - self.x1)
        self.audio_manager.set_volume(self.volume)

'''
class ArrowButton:
    def __init__(self, x, y, width, height, direction) -> None:
        self.image = pygame.Surface([width, height],pygame.SRCALPHA)
        self.colour = (255,255,255)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        self.direction = direction  # 'left' or 'right'
    
    def draw_arrow(self):
        points = []
        if self.direction == 'left':
            points = [(self.rect.width, 0), (0, self.rect.height//2), (self.rect.width, self.rect.height)]
        elif self.direction == 'right':
            points = [(0,0), (self.rect.width, self.rect.height//2), (0, self.rect.height)]
        
        self.image.fill((0, 0, 0, 0))
        pygame.draw.polygon(self.image, self.colour, points)
    
    def arrow_clicks(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #for left arrow
                if self.direction=='left':
                    if (self.rect.x <= mouse_x <= self.rect.x + self.rect.width and self.rect.y <= mouse_y <= self.rect.y + self.rect.height):
                        audio_manager.next_song()
                elif self.direction=='right':
                    if (self.rect.x <= mouse_x <= self.rect.x + self.rect.width and self.rect.y <= mouse_y <= self.rect.y + self.rect.height):
                        audio_manager.prev_song()

'''
#initialize instance and run
if __name__ == '__main__':
    game_screen1 = OptionsScreen()
    game_screen1.run()