import pygame
import sys
from question2 import Question
import Boss
import Player

# Initialize Pygame
pygame.init()

# Screen setup
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Trivia Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load the image
image_path = 'images/level1MathApple.png'  # Replace with your image file's path
image = pygame.image.load(image_path)
imageResized = pygame.transform.scale(image, (80,80))


# Font setup
font = pygame.font.Font(None, 36)

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

"""
Set up Boss and Player
"""
boss = Boss()
player = Player("natetyu", 100, 0, 1)


"""
Hardcoded question to be displayed
"""
q = Question(1, "What is the perimeter of a rectangle with diagonal length 17 units and length 8 units?", ["1","2","3","4"], "2", 4, False, "Math")

# Function to draw buttons and check for clicks
def draw_button(text, x, y, width, height, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button_rect = pygame.Rect(x, y, width, height)

    if button_rect.collidepoint(mouse):
        pygame.draw.rect(screen, GREEN, button_rect)
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, WHITE, button_rect)

    draw_text(text, font, BLACK, screen, x + 10, y + 10)

def check_answer(answer):
    if answer == q.correctAnswer:
        print("Correct!")
    else:
        print("Incorrect!")

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    """
    Render image
    """
    screen.blit(imageResized, (150, 250))

    """
    Check if length of string can fit in the window, if not then lower font size
    """
    if (len(q.prompt) > 50):
        font = pygame.font.Font(None, 24)
    
    # Draw question
    draw_text(q.prompt, font, BLACK, screen, 100, 100)
    
    # Draw answer buttons
    for i, answer in enumerate(q.choices):
        button_x = 100 + (i % 2) * 300
        button_y = 400 + (i // 2) * 100
        draw_button(answer, button_x, button_y, 200, 50, lambda a=answer: check_answer(a))

    pygame.display.flip()

pygame.quit()
sys.exit()
