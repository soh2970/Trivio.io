import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Math Symbols in Pygame GUI")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Define mathematical symbols
subset_symbol = "⊂"
pi_symbol = "π"

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Render text with mathematical symbols
    subset_text = font.render("Subset: " + subset_symbol, True, BLACK)
    pi_text = font.render("Pi: " + pi_symbol, True, BLACK)

    # Blit text onto the screen
    screen.blit(subset_text, (50, 100))
    screen.blit(pi_text, (50, 150))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()