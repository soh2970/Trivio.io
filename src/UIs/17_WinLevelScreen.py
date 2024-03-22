'''
Win level screen
displays win and player stats
'''
import pygame
import sys
import math

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
width = screen.get_width()
height = screen.get_height()
# fills the screen with a color: white 
white = (255,255,255)
screen.fill(white)
# set screen name
pygame.display.set_caption('Trivio')
# update game screen
pygame.display.update()

#font
smallfont = pygame.font.SysFont('Corbel',20) 
bigfont= pygame.font.SysFont('Corbel',140) 

#text
text1 = bigfont.render('LEVEL', True, (0, 0, 0))
textRect1 = text1.get_rect(center = (width//2, height/12*5))
text2 = bigfont.render('PASSED', True, (0, 0, 0))
textRect2 = text2.get_rect(center = (width//2, height/12*7))

#line
pygame.draw.line(screen, "Black", (width/3,height/12*8), (width/3*2, height/12*8), 1)

# buttons
button_colour1 = (159,197,248)
level_button = pygame.draw.rect(screen, (0,0,0), (width/5*4, height/15*13, 80,30),1)
next_level_text = smallfont.render("Next Level", (level_button.centerx, level_button.centery), (0,0,0))
next_level_rect = next_level_text.get_rect(center = level_button.center)

save_button = pygame.draw.rect(screen, button_colour1, (width/5*4, height/15*1, 80,30))
save_border = pygame.draw.rect(screen, (0,0,0), (width/5*4, height/15*1, 80,30), 1)
save_text = smallfont.render("Save Game", (save_button.centerx, save_button.centery), (0,0,0))
save_rect = save_text.get_rect(center = save_button.center)

options_button = pygame.draw.rect(screen, button_colour1, (width/5*4, height/15*2, 80,30))
options_border = pygame.draw.rect(screen, (0,0,0), (width/5*4, height/15*2, 80,30), 1)
options_text = smallfont.render("Options", (options_button.centerx, options_button.centery), (0,0,0))
options_rect = options_text.get_rect(center = options_button.center)

# update game screen  
pygame.display.update()

# boolean variable to check if the exit button has been clicked or not
running = True
# keep game running till running is true 
while running: 
    # display text
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    # display buttons
    screen.blit(next_level_text, next_level_rect)
    screen.blit(options_text, options_rect)
    screen.blit(save_text, save_rect)
    #update displaay
    pygame.display.update()
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