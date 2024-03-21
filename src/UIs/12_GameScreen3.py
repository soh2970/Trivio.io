import pygame
import sys
import random
import json
import datetime
from Game import Game

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

# Load images
boss1_image_path = 'images/level1MathApple.png'
boss1_image = pygame.image.load(boss1_image_path)
boss1_image_resized = pygame.transform.scale(boss1_image, (80, 80))

boss2_image_path = 'images/level2MathApple.png'
boss2_image = pygame.image.load(boss2_image_path)
boss2_image_resized = pygame.transform.scale(boss2_image, (80, 80))

boss3_image_path = 'images/level3MathApple.png'
boss3_image = pygame.image.load(boss3_image_path)
boss3_image_resized = pygame.transform.scale(boss3_image, (80, 80))

player1_image_path = 'images/userLevel1.png'
player1_image = pygame.image.load(player1_image_path)
player1_image_resized = pygame.transform.scale(player1_image, (80, 80))

player2_image_path = 'images/userLevel2.png'
player2_image = pygame.image.load(player2_image_path)
player2_image_resized = pygame.transform.scale(player2_image, (80, 80))

player3_image_path = 'images/userLevel3.png'
player3_image = pygame.image.load(player3_image_path)
player3_image_resized = pygame.transform.scale(player3_image, (80, 80))

player_lose_image_path = 'images/userLose.jpeg'
player_lose_image = pygame.image.load(player_lose_image_path)
player_lose_image_resized = pygame.transform.scale(player_lose_image, (80, 80))

# Font setup
font = pygame.font.Font(None, 36)

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

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

# Initialize the game
game = Game()
game.startGame("natetyu")
game.presentQuestion()

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render boss image based on boss health
    boss_hp = game.boss.getBossHp()
    if 80 <= boss_hp <= 100:
        screen.blit(boss1_image_resized, (200, 200))
    elif 50 <= boss_hp < 80:
        screen.blit(boss2_image_resized, (200, 200))
    elif 0 < boss_hp < 50:
        screen.blit(boss3_image_resized, (200, 200))

    # Render player image based on player health
    player_hp = game.player.getPlayerHP()
    if 80 <= player_hp <= 100:
        screen.blit(player1_image_resized, (500, 200))
    elif 50 <= player_hp < 80:
        screen.blit(player2_image_resized, (500, 200))
    elif 0 < player_hp < 50:
        screen.blit(player3_image_resized, (500, 200))
    elif player_hp == 0:
        screen.blit(player_lose_image_resized, (500, 200))

    # Render question
    question = game.presentQuestion()
    draw_text(question.question, font, BLACK, screen, 100, 100)

    # Render answer buttons
    for i, answer in enumerate(question.options):
        button_x = 100 + (i % 2) * 300
        button_y = 400 + (i // 2) * 100
        draw_button(answer, button_x, button_y, 200, 50)

    pygame.display.flip()

pygame.quit()
sys.exit()
