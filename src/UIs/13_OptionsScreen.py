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

        """
        need to find way to add list or dictionary with the song choices
        """

        

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
        self.image = pygame.Surface([width, height])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        self.direction = direction  # 'left' or 'right'

    def arrow_clicks(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.direction=='left' and (self.rect.width-self.rect.x) <= pygame.mouse.get_pos <= self.rect.width and (self.rect.height-self.rect.y) <= pygame.mouse.get_pos() <= self.rect.height:
                    self.current_song_index = (self.current_song_index - 1) % len(songs)
                    self.change_song()
                elif self.direction=='right' and self.rect.width <= pygame.mouse.get_pos() <= (self.rect.width+self.rect.x) and self.rect.height <= pygame.mouse.get_pos() <= (self.rect.height+self.rect.y):
                    self.current_song_index = (self.current_song_index - 1) % len(songs)
    
    def change_song(self):
        pygame.mixer.music.stop()
        current_song = songs[self.current_song_index]['path']
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play(-1)

    def draw_current_song(self):
        song_name = songs[self.current_song_index]['name']
        font = pygame.font.SysFont(None, 24)
        text_surface = font.render(song_name, True, (255,255,255))
        self.screen.blit(text_surface, (100, 50))


#initialize instance and run
if __name__ == '__main__':
    game_screen1 = OptionsScreen()
    game_screen1.run()