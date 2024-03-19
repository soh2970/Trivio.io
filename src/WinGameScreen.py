import pygame
import sys

# initializing the constructor 
pygame.init() 

# DISPLAY
# screen resolution 
initial_size = (844,600) 
screen = pygame.display.set_mode(initial_size, pygame.RESIZABLE) 
# constant sizes
MIN_WIDTH = 844
MIN_HEIGHT = 600 
# get width and height of screen
width = screen.get_width
height = screen.get_height
# fills the screen with a color: white 
white = (255,255,255)
screen.fill(white)
# set screen name
pygame.display.set_caption('Trivio')
# update game screen
pygame.display.update()



# boolean variable to check if the exit button has been clicked or not
running = True
# keep game running till running is true 
while running: 
      
    # check for event if user has pushed any event in queue 
    for event in pygame.event.get(): 
          
        # user quits
        if event.type == pygame.QUIT: 
            running = False
        # user resizing screen
        elif event.type == pygame.VIDEORESIZE:
            # check if the new size is below the minimum size
            new_width = max(event.w, MIN_WIDTH)
            new_height = max(event.h, MIN_HEIGHT)

             # resize window if below min
            if new_width<event.w or new_height != event.h:
                window = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
            else:
                # increase size
                window_size = (event.w, event.h)
                window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

# update game screen
pygame.display.update()