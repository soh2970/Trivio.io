import pygame 
import sys
import os

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)


from src.UIs.screen import ScreenBase

class LoseGameScreen(ScreenBase):
    def __init__(self, category, level, hp, questions_right, questions_wrong, score, width, height):
        super().__init__(width, height)  # Initialize with ScreenBase settings
        self.type = 'loseGameScreen'
        self.category = category
        self.level = level
        self.hp = hp
        self.questions_right = questions_right
        self.questions_wrong = questions_wrong
        self.score = score
        self.transitionToLeaderboard = False
        
    def draw(self):
        super().draw()
        # get the current width and height of the screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        # Create a rect for the "Next" button
        self.next_button = pygame.Rect(700, 550, 90, 30)

        # Draw the header text
        header_text = self.HEADING_FONT.render('DEFEAT', True, self.BLACK)
        self.screen.blit(header_text, (self.width/2-170, self.width/2-350))

        # Load the image
        # Since the Python file is in src/UI and the image is in src/image,
        # the relative path to the image is '../image/rip.png'
        images_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'images')
        image_path = os.path.join(images_dir, 'rip.png')
        self.rip_image = pygame.image.load(image_path)

        # Resize the image
        new_width, new_height = 300, 300  # New dimensions for the image
        self.rip_image = pygame.transform.scale(self.rip_image, (new_width, new_height))
        # Draw the rip images
        self.screen.blit(self.rip_image, (self.width/100*6, self.height/4))
        self.screen.blit(self.rip_image, (self.width/10*6, self.height/4))

        # Draw the  message
        lost_text = self.SMALLER_FONT.render('You lost to boss!', True, self.BLACK)
        self.screen.blit(lost_text, (self.width/2-100, self.width/2-260))
        stats_text = self.SMALLER_FONT.render('Here are your stats:', True, self.BLACK)
        self.screen.blit(stats_text, (self.width/2-110, self.width/2-230))
        category_text = self.SMALLER_FONT.render(f'Category:{self.category}', True, self.BLACK)
        self.screen.blit(category_text, (self.width/2-110, self.width/2-200))
        level_text = self.SMALLER_FONT.render(f'Level:{self.level}', True, self.BLACK)
        self.screen.blit(level_text, (self.width/2-110, self.width/2-170))
        hp_text = self.SMALLER_FONT.render(f'Boss HP:{self.hp}', True, self.BLACK)
        self.screen.blit(hp_text, (self.width/2-110, self.width/2-140))
        right_text = self.SMALLER_FONT.render(f'Questions Right:{self.questions_right}', True, self.BLACK)
        self.screen.blit(right_text, (self.width/2-110, self.width/2-110))
        wrong_text = self.SMALLER_FONT.render(f'Questions Wrong:{self.questions_wrong}', True, self.BLACK)
        self.screen.blit(wrong_text, (self.width/2-110, self.width/2-80))


        # Draw the "Next" button
        pygame.draw.rect(self.screen, self.BLUE, self.next_button)
        button_text = self.SMALLER_FONT.render('Next', True, self.BLACK)
        self.screen.blit(button_text, (715, 555))

    def handle_events(self):
            # stores the (x,y) coordinates into the variable as a tuple
            mouse = pygame.mouse.get_pos() 
            for event in pygame.event.get():
                    # user quits
                if event.type == pygame.QUIT: 
                    running = False
                # user resizing screen
                elif event.type == pygame.VIDEORESIZE:
                    # check if the new size is below the minimum size
                    new_width = max(event.w, self.MIN_WIDTH)
                    new_height = max(event.h, self.MIN_HEIGHT)
                    new_width = max(event.w, self.MIN_WIDTH)
                    new_height = max(event.h, self.MIN_HEIGHT)

                    # resize window if below min
                    if new_width<event.w or new_height != event.h:
                        window = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
                    else:
                        # increase size
                        window_size = (event.w, event.h)
                        window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the "Next" button was clicked
                    if self.next_button.collidepoint(event.pos):
                        self.transitionToLeaderboard = True
                        

    def run(self):
        super().run()


#initialize instance and run
if __name__ == '__main__':
    game_screen1 = LoseGameScreen()
    game_screen1.run()
