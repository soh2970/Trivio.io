import pygame
import sys
import os
import json
from screen import ScreenBase
from GameScreenButtons import GameScreenButtons

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)


#please ignore or alter this path as where your json file is located.
os.chdir("C:\\Users\\kimgu\\2212\\repositories2212\\personalRepo2212\\src")
print(os.getcwd())

class DebuggerModeScreen(ScreenBase):
    """

    """

    def __init__(self, screen, category=None, level=None):
        super().__init__()
        self.screen = screen
        self.category = category
        self.level = level
        self.questions = []
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.load_questions()

        self.back_button = GameScreenButtons(10, 10, 100, 40, 'Back', self.on_back)
        self.home_button = GameScreenButtons(120, 10, 100, 40, 'Home', self.on_home)
        # Define scroll start offset
        self.scroll_offset = 0
        self.start = 0
        self.end = 10

        self.scrollbar_rect = pygame.Rect(self.screen.get_width() - 20, 100, 20, self.screen.get_height() - 100)
        self.is_dragging = False

    #room to use DebuggerMode class for load_questions
    def load_questions(self):
        with open(os.path.join(src_dir, 'testbank.json'), 'r', encoding='utf-8') as file:
            test_bank = json.load(file)
        self.questions = test_bank['subjects'].get(self.category, {}).get(self.level, [])

    def on_back(self):
        # Placeholder for the back button logic -> main script transitions
        print("Back button pressed")

    def on_home(self):
        # Placeholder for the home button logic -> main script transitions
        print("Home button pressed")


    def draw(self):
        self.screen.fill(self.WHITE)
        self.back_button.draw(self.screen)
        self.home_button.draw(self.screen)
        
        # Constants for layout
        max_visible_rows = 10
        line_height = self.MODE_FONT.get_height() + 20  # Increase line height for more space
        content_start_y = 150
        scrollbar_width = 20

        # Draw the column labels
        question_number_label_x = 50
        question_label_x = 150
        answer_label_x = self.screen.get_width() // 2

        #titles
        category = self.SMALLER_FONT.render(f"{self.category}: {self.level}", True, self.BLACK)

        # Draw the column labels
        start = self.BUTTON_FONT.render(f'{self.category}: Level {self.level}', True, 0)
        self.screen.blit(self.SMALLER_FONT.render("Question #", True, self.BLACK), (question_number_label_x, content_start_y))
        self.screen.blit(self.SMALLER_FONT.render("Question", True, self.BLACK), (question_label_x, content_start_y))
        self.screen.blit(self.SMALLER_FONT.render("Answer", True, self.BLACK), (answer_label_x, content_start_y))
        self.screen.blit(start, (self.width/2+220,self.height/2+60))
        # Define the area where the questions and answers will be displayed
        content_rect = pygame.Rect(0, content_start_y + line_height, self.screen.get_width() - scrollbar_width, max_visible_rows * line_height)
        
        # Enable clipping to content area
        self.screen.set_clip(content_rect)

        y_offset = content_start_y + line_height - self.scroll_offset
        question_number_x = question_number_label_x
        question_x = question_label_x
        answer_x = answer_label_x

        # Draw questions and answers within the content area
        for index, question in enumerate(self.questions, start=1):
            if content_start_y < y_offset < content_start_y + content_rect.height:
                self.screen.blit(self.MODE_FONT.render(f"{index}.", True, self.BLACK), (question_number_x, y_offset))
                self.screen.blit(self.MODE_FONT.render(question['question'], True, self.BLACK), (question_x, y_offset))
                self.screen.blit(self.MODE_FONT.render(question['correctAnswer'], True, self.BLACK), (answer_x, y_offset))
            y_offset += line_height

        # Disable clipping
        self.screen.set_clip(None)

        # Draw scrollbar background
        scrollbar_rect = pygame.Rect(self.screen.get_width() - scrollbar_width, content_start_y, scrollbar_width, content_rect.height)
        pygame.draw.rect(self.screen, self.GREY, scrollbar_rect)

        # Draw scrollbar thumb
        total_content_height = len(self.questions) * line_height
        thumb_height = max(content_rect.height * content_rect.height / total_content_height, 20)  # Minimum thumb height for visibility
        thumb_y = content_rect.y + (self.scroll_offset / total_content_height) * content_rect.height
        thumb_rect = pygame.Rect(scrollbar_rect.x, thumb_y, scrollbar_width, thumb_height)
        pygame.draw.rect(self.screen, self.BLUE, thumb_rect)
        
        pygame.display.flip()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle button clicks
                if self.back_button.rect.collidepoint(event.pos):
                    self.back_button.callback()
                elif self.home_button.rect.collidepoint(event.pos):
                    self.home_button.callback()
                
                # Scroll up
                if event.button == 4:
                    self.scroll_offset = max(self.scroll_offset - 15, 0)
                # Scroll down
                elif event.button == 5:
                    self.scroll_offset = min(self.scroll_offset + 15, self.get_max_scroll())
            elif event.type == pygame.VIDEORESIZE:
                self.resize_screen(event)

    def get_max_scroll(self):
        total_question_height = len(self.questions) * (self.BASE_FONT.get_height() + 20)
        return max(0, total_question_height - self.MIN_HEIGHT)
    

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()