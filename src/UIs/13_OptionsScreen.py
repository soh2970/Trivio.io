"""
Options Screen
gives players options to change aspects 
Add a reset button

"""
from screen import ScreenBase
import pygame
import os
import sys

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)

class OptionsScreen(ScreenBase):

    def __init__(self):
        super().__init__()
        # get the current width and height of the screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        

        #slider values
        self.slider_pos = self.width/5*3  # Initial slider position
        self.slider_max = self.width/5*4  # Maximum x-coordinate for the slider
        self.slider_min = self.width/5*2  # Minimum x-coordinate for the slider
        self.slider_y = self.height/12*5    # Y-coordinate for the slider
        self.is_dragging = False  # Track whether the slider is being dragged


    def draw(self):
        super().draw()

        #text
        self.text1 = self.MEDIUM_FONT.render('Options', True, self.BLACK)
        self.textRect1 = self.text1.get_rect(center = (self.width//2, self.height/12*3))
        self.volume_text = self.BUTTON_FONT.render('VOLUME', True, self.BLACK)
        self.vol_textrect = self.volume_text.get_rect(center = (self.width/5, self.height/12*5))
        self.song_text = self.BUTTON_FONT.render('SONG', True, self.BLACK)
        self.song_textrect = self.song_text.get_rect(center = (self.width/5, self.height/12*7))
        self.brightness_text = self.BUTTON_FONT.render('DISPLAY', True, self.BLACK)
        self.brightness_textrect = self.brightness_text.get_rect(center = (self.width/5, self.height/12*9))
        
        #slider
        
        # Draw the slider bar
        pygame.draw.line(self.screen, self.BLACK, (self.slider_min, self.slider_y), (self.slider_max, self.slider_y), 3)
        # Draw the slider button
        pygame.draw.circle(self.screen, self.BLACK, (self.slider_pos, self.slider_y), 10)
        
        
        #arrows

        #buttons
        self.light_button = pygame.draw.rect(self.screen, self.BLACK, (self.width/5*2, self.height/15*10.5, 160,60),1)
        self.light_button_text = self.SMALLER_FONT.render("Light", (self.light_button.centerx, self.light_button.centery), self.BLACK)
        self.light_button_textrect = self.light_button_text.get_rect(center = self.light_button.center)
        self.dark_button = pygame.draw.rect(self.screen, self.DARKGREY, (self.width/5*3, self.height/15*10.5, 160,60))
        self.dark_button_text = self.SMALLER_FONT.render("Dark", (self.dark_button.centerx, self.dark_button.centery), self.WHITE)
        self.dark_button_textrect = self.dark_button_text.get_rect(center = self.dark_button.center)

        # display text
        self.screen.blit(self.text1, self.textRect1)
        self.screen.blit(self.volume_text, self.vol_textrect)
        self.screen.blit(self.song_text, self.song_textrect)
        self.screen.blit(self.brightness_text, self.brightness_textrect)

        #display buttons
        self.screen.blit(self.light_button_text, self.light_button_textrect)
        self.screen.blit(self.dark_button_text, self.dark_button_textrect)



    def handle_events(self):
        # stores the (x,y) coordinates into the variable as a tuple
        self.mouse = pygame.mouse.get_pos() 

        for event in pygame.event.get():
            # user quits
            if event.type == pygame.QUIT: 
                self.running = False
                pygame.quit()
                sys.exit()
            # user resizing screen
            elif event.type == pygame.VIDEORESIZE:
                super().resize_screen(event)
            # user clicking
            if event.type == pygame.MOUSEBUTTONDOWN:
                if abs(event.pos[0] - self.slider_pos) < 10 and abs(event.pos[1] - self.slider_y) < 10:
                    self.is_dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.is_dragging = False
            elif event.type == pygame.MOUSEMOTION and self.is_dragging:
                self.slider_pos = min(max(event.pos[0], self.slider_min), self.slider_max)

    def adjust_volume(self):
        volume = (self.slider_pos - self.slider_min) / (self.slider_max - self.slider_min)
        pygame.mixer.music.set_volume(volume)
    
    def run(self):
        super().run()

class ArrowButton:
    def __init__(self, colour, x, y, width, height, direction) -> None:
        pass

#initialize instance and run
if __name__ == '__main__':
    game_screen1 = OptionsScreen()
    game_screen1.run()