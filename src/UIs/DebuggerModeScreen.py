import pygame
import sys
# import os
import json
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons


# # Get the absolute path to the src directory
# src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
# sys.path.append(src_dir)

<<<<<<< HEAD


#please ignore or alter this path as where your json file is located.
=======
from src.UIs.screen import ScreenBase
from src.UIs.GameScreenButtons import GameScreenButtons


#please ignore or alter this path as where your json file is located.
# os.chdir("C:\\Users\\kimgu\\2212\\repositories2212\\personalRepo2212\\src")
# print(os.getcwd())
>>>>>>> 169d1aaef30e32dda263f35a8608461c670d1e4e

class DebuggerModeScreen(ScreenBase):
    """
    
    """
    content_start_y = 150
    def __init__(self, category=None, level=None):
        super().__init__()
        self.category = category
        self.level = level
        self.questions = []
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.type = "debuggerModeScreen"
        self.transitionToLogin = False
        self.load_questions()

        self.back_button = GameScreenButtons(10, 10, 100, 40, 'Back', self.on_back, (0, 0, 0), (255,255,255))

        self.home_button = GameScreenButtons(120, 10, 100, 40, 'Home', self.on_home, (0,0,0), (255,255,255))
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
        self.transitionToLogin = True


    def draw(self):
        self.screen.fill(self.WHITE)
        self.back_button.draw(self.screen)
        self.home_button.draw(self.screen)
        
        # Constants for layout
        line_height = self.MODE_FONT.get_height() + 20  # Increase line height for more space
        content_start_y = self.content_start_y
        scrollbar_width = 20
        space_between_columns = 200  # Increase space between columns
        title_padding = 60

        category_mapping = {
        "math": "Math",
        "social_sciences": "Social Sciences",
        "science": "Science"
        }
        category_display = category_mapping.get(self.category, self.category).replace("_", " ").title()
    
        # Adjust the level for display
        level_display = self.level.replace("level", "Level ").capitalize()
        
        # Measure the column label widths
        question_number_label = self.SMALLER_FONT.render("Question #", True, self.BLACK)
        question_label = self.SMALLER_FONT.render("Question", True, self.BLACK)
        answer_label = self.SMALLER_FONT.render("Answer", True, self.BLACK)

        # Set the x-coordinates for the columns based on the label widths
        total_columns_width = question_number_label.get_width() + question_label.get_width() + answer_label.get_width() + (2 * space_between_columns)
        start_x = (self.width - total_columns_width - scrollbar_width) // 2  # Centering the total width on the screen

        question_number_label_x = start_x
        question_label_x = question_number_label_x + question_number_label.get_width() + space_between_columns
        answer_label_x = question_label_x + question_label.get_width() + space_between_columns

        # Draw the column labels
        self.screen.blit(question_number_label, (question_number_label_x, content_start_y - line_height))
        self.screen.blit(question_label, (question_label_x, content_start_y - line_height))
        self.screen.blit(answer_label, (answer_label_x, content_start_y - line_height))

        # Render the title text
        title_text_str = f"{category_display}: {level_display}"
        title_text = self.MID_FONT.render(title_text_str, True, self.BLACK)
        title_width = title_text.get_width()
        
        # Center the title text above the Question column
        title_position_x = question_label_x + (question_label.get_width() - title_width) // 2
        title_position_y = content_start_y - line_height - title_padding  # Space above the question label
        
        # Draw the title text
        self.screen.blit(title_text, (title_position_x, title_position_y))

        # Content area for questions and answers
        content_height = self.height - content_start_y - 30  # Slightly reduce the content height to prevent cut-off
        content_rect = pygame.Rect(0, content_start_y, self.width - scrollbar_width, content_height)

        # Enable clipping to content area
        self.screen.set_clip(content_rect)

        # Variables to offset the y position based on the current scroll
        y_offset = content_start_y - self.scroll_offset

        # Draw questions and answers within the content area
        for index, question in enumerate(self.questions):
            current_y_position = y_offset + index * line_height
            item_bottom_position = current_y_position + line_height
            # Only draw if the entire item fits within the content area
            if item_bottom_position <= content_start_y + content_rect.height:
                question_text = self.MODE_FONT.render(f"{index + 1}.", True, self.BLACK)
                answer_text = self.MODE_FONT.render(question['question'], True, self.BLACK)
                correct_answer_text = self.MODE_FONT.render(question['correctAnswer'], True, self.BLACK)

                # Center the text within each column
                self.screen.blit(question_text, (question_number_label_x + (question_number_label.get_width() - question_text.get_width()) // 2, current_y_position))
                self.screen.blit(answer_text, (question_label_x + (question_label.get_width() - answer_text.get_width()) // 2, current_y_position))
                self.screen.blit(correct_answer_text, (answer_label_x + (answer_label.get_width() - correct_answer_text.get_width()) // 2, current_y_position))

        # Disable clipping
        self.screen.set_clip(None)

        # Draw scrollbar background (slightly wider and with a light color)
        scrollbar_background_rect = pygame.Rect(self.screen.get_width() - 25, content_start_y, 15, content_rect.height)
        pygame.draw.rect(self.screen, self.GREY, scrollbar_background_rect)

        # Calculate scrollbar thumb properties (more stylized with rounded corners)
        total_content_height = len(self.questions) * line_height
        thumb_height = max(scrollbar_background_rect.height * scrollbar_background_rect.height / total_content_height, 20)  # Ensure minimum thumb height for visibility
        thumb_y = content_start_y + (self.scroll_offset / total_content_height) * scrollbar_background_rect.height
        thumb_rect = pygame.Rect(self.screen.get_width() - 23, thumb_y, 11, thumb_height)  # Slightly narrower thumb for aesthetics
        thumb_color = self.DARKGREY  # Darker color for the thumb

        # Draw scrollbar thumb with rounded corners
        pygame.draw.rect(self.screen, thumb_color, thumb_rect, border_radius=5)
        
        # Draw the outline for the scrollbar (optional)
        pygame.draw.rect(self.screen, self.BLACK, scrollbar_background_rect, 2, border_radius=5)  # Outline for the scrollbar with rounded corners

        pygame.display.flip()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle button clicks
                if self.back_button.rect1.collidepoint(event.pos):
                    self.back_button.callback()
                elif self.home_button.rect1.collidepoint(event.pos):
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
        # Calculate the height of all content and the space required for one additional line
        total_content_height = len(self.questions) * (self.MODE_FONT.get_height() + 20)
        # Calculate the visible content area
        visible_content_height = self.height - self.content_start_y
        # Maximum scroll offset is the space required beyond the visible area
        return max(0, total_content_height - visible_content_height)


    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()