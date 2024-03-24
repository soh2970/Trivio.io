

class RadioButton(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, font, text):
        super().__init__() 
        text_surf = font.render(text, True, (0, 0, 0))
        self.button_image = pygame.Surface((w, h))
        self.button_image.fill((228, 246, 248))
        self.button_image.blit(text_surf, text_surf.get_rect(center = (w // 2, h // 2)))
        self.hover_image = pygame.Surface((w, h))
        self.hover_image.fill((228, 246, 248))
        self.hover_image.blit(text_surf, text_surf.get_rect(center = (w // 2, h // 2)))
        pygame.draw.rect(self.hover_image, (0,71,100), self.hover_image.get_rect(), 5)
        self.clicked_image = pygame.Surface((w, h))
        self.clicked_image.fill((135,206,250))
        self.clicked_image.blit(text_surf, text_surf.get_rect(center = (w // 2, h // 2)))
        self.image = self.button_image
        self.rect = pygame.Rect(x, y, w, h)
        self.clicked = False
        self.buttons = None

    def setRadioButtons(self, buttons):
        self.buttons = buttons

    def update(self, event_list):
        hover = self.rect.collidepoint(pygame.mouse.get_pos())
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover and event.button == 1:
                    for rb in self.buttons:
                        rb.clicked = False
                    self.clicked = True
        
        self.image = self.button_image
        if self.clicked:
            self.image = self.clicked_image
        elif hover:
            self.image = self.hover_image


pygame.init()
screen = pygame.display.set_mode((844, 600))
clock = pygame.time.Clock()
font50 = pygame.font.SysFont(None, 50)
#back button
smallfont = pygame.font.SysFont('Corbel',32) 
back = smallfont.render('Back' , True , 0) 

#start tutorial button
start = smallfont.render('Start Tutorial >>', True, 0)

#texts on screen
bigfont = pygame.font.SysFont('Corbel',50)
mode = bigfont.render('Mode Selection', True, 0)
categories = smallfont.render('Select a Category to start', True, 0)
category_text = smallfont.render('Category', True, 0)



radioButtons = [
    RadioButton(560, 280, 270, 60, font50, "Math"),
    RadioButton(290, 280, 270, 60, font50, "Social Science"),
    RadioButton(20, 280, 270, 60, font50, "Science")
]
for rb in radioButtons:
    rb.setRadioButtons(radioButtons)
radioButtons[0].clicked = True

group = pygame.sprite.Group(radioButtons)

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            
            #if the mouse is clicked on the 
            # x button the game is terminated 
            if width/2-400 <= mouse[0] <= width /2-340 and height/2-293 <= mouse[1] <= height/2-263: 
                pygame.quit() #CHANGE to previous screen New/Save mode
            if width/2+215 <= mouse[0] <= width /2+395 and height/2+50 <= mouse[1] <= height/2+90: 
                pygame.quit() #CHANGE to next tutorial screen 
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
    group.update(event_list)

    screen.fill((255,255,255))
    #back button display
    pygame.draw.rect(screen,color_back,[width/2-400,height/2-293,60,30]) 
    screen.blit(back , (width/2-397,height/2-290)) 


    screen.blit(categories, (width/2-140,height/2-180))
    screen.blit(mode, (width/2-130, height/2-230))
    screen.blit(category_text, (width/2-370, height/2-60))

    #start tutorial button
    pygame.draw.rect(screen,color_button,[width/2+215,height/2+50,180,40]) 
    screen.blit(start, (width/2+220,height/2+60))

    group.draw(screen)
    pygame.display.flip()

pygame.quit()
exit()

from screen import ScreenBase
import pygame
import sys
import os

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)
# initializing the constructor 
pygame.init() 

class GameModeSelectScreen(ScreenBase):

    def __init__(self):
        super().__init__()

    def draw(self):
        super().draw()

    def handle_events(self):
        # call parent class event handling
        super().handle_events()

    def run(self):
        super().run()

#initialize instance and run
if __name__ == '__main__':
    game_screen1 = GameModeSelectScreen()
    game_screen1.run()