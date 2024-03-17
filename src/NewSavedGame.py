import pygame
import sys

# initializing Pygame
pygame.init()

# screen resolution
res = (990, 620)

# create the screen
screen = pygame.display.set_mode(res)

# colors
color_black = (0, 0, 0)
color_green = (0, 255, 0)
color_light_blue = (173, 216, 230)  # Light blue color
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
            if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 30:
                running = False

    # fill the screen with white
    screen.fill(color_white)

    # draw the buttons
    pygame.draw.circle(screen, color_green, (width/4, height/2), 100)
    pygame.draw.circle(screen, color_light_blue, (3*width/4, height/2), 100)

    # put the text on the buttons
    screen.blit(text_new_game, (width/4 - text_new_game.get_width()/2, height/2 - text_new_game.get_height()/2))
    screen.blit(text_saved_game, (3*width/4 - text_saved_game.get_width()/2, height/2 - text_saved_game.get_height()/2))

    # draw close button
    pygame.draw.rect(screen, color_grey, [5, 5, 50, 30])  # Adjusted size to match your example
    screen.blit(text_esc, (5, 0))  # Positioned to match your example

    # update the display
    pygame.display.update()

# quit Pygame
pygame.quit()
