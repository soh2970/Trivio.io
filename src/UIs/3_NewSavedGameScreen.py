import pygame
import sys
import os

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)

# initializing Pygame
pygame.init()

# screen resolution
res = (844,600) 

# create the screen
screen = pygame.display.set_mode(res)

# colors
color_black = (0, 0, 0)
color_green = (204, 245, 205)
color_light_blue = (159, 197, 248)  # Light blue color
color_white = (255, 255, 255)
color_grey = (220, 220, 220)  # Grey color for the close button

# screen width and height
width = screen.get_width()
height = screen.get_height()

# fonts
font = pygame.font.SysFont('Corbel', 35)
# Larger font for the close button to match your example
font_esc = pygame.font.SysFont('Corbel', 60)

# text for buttons
text_new_game = font.render('New Game', True, color_black)
text_saved_game = font.render('Saved Game', True, color_black)
text_esc = font_esc.render('x', True, color_black)
text_or = font_esc.render('OR',True, color_black )

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # get mouse position
            mouse = pygame.mouse.get_pos()

            # close button (top left corner)
            if width/2-405 <= mouse[0] <= width/2-385 and height/2-293 <= mouse[1] <= height/2-263: 
                pygame.quit() 

    # fill the screen with white
    screen.fill(color_white)

    # draw the buttons
    pygame.draw.circle(screen, color_green, (width/4, height/2), 100)
    pygame.draw.circle(screen, color_light_blue, (3*width/4, height/2), 100)

    # put the text on the buttons
    screen.blit(text_new_game, (width/4 - text_new_game.get_width()/2, height/2 - text_new_game.get_height()/2))
    screen.blit(text_saved_game, (3*width/4 - text_saved_game.get_width()/2, height/2 - text_saved_game.get_height()/2))

    # draw close button
    pygame.draw.rect(screen,color_grey,[width/2-405,height/2-293,30,30]) 
    screen.blit(text_esc , (width/2-400,height/2-300)) 

    #put or on the screen
    screen.blit(text_or, (width/2-25, height/2-10))


    # update the display
    pygame.display.update()

# quit Pygame
pygame.quit()
