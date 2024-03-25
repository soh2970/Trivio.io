import pygame
import sys
import os
from GameScreenButtons import GameScreenButtons
import json

# Get the absolute path to the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_dir)


class RadioButton(pygame.sprite.Sprite):
    """
    A RadioButton is a visual element that can be selected or deselected.

    Attributes:
        button_image (pygame.Surface): The default image of the button when not interacted with.
        hover_image (pygame.Surface): The image of the button when the mouse hovers over it.
        clicked_image (pygame.Surface): The image of the button when it has been clicked and selected.
        image (pygame.Surface): The current image of the button being displayed.
        rect (pygame.Rect): The rectangle area that the button covers.
        clicked (bool): Indicates whether the button is currently selected.
        buttons (list): A list of other radio button instances that this button is grouped with.

    Methods:
        setRadioButtons(buttons): Associates this radio button with a group of other radio buttons.
        update(event_list): Updates the button's state based on the provided events.
    """

    def __init__(self, x, y, w, h, font, text):
        super().__init__()
        self.text = text
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



class DebuggerDashboardPage:
    """
    The main page for the debugger dashboard interface where the user can select
    a category and a level before proceeding to the next stage.

    Attributes:
        screen (pygame.Surface): The screen onto which the dashboard will be rendered.
        clock (pygame.time.Clock): A clock object to control the frame rate.
        font (pygame.font.Font): The font used for regular text.
        big_font (pygame.font.Font): The font used for headers.
        bg_color (tuple): The background color of the dashboard.
        text_color (tuple): The color of the text.
        header_text (pygame.Surface): Rendered surface of the header text.
        subheader_text (pygame.Surface): Rendered surface of the subheader text.
        category_label (pygame.Surface): Rendered surface of the 'Category' label.
        level_label (pygame.Surface): Rendered surface of the 'Level' label.
        home_button (GameScreenButtons): The 'Home' button instance.
        next_button (GameScreenButtons): The 'Next' button instance.
        category_buttons (list): List of 'RadioButton' instances for categories.
        level_buttons (list): List of 'RadioButton' instances for levels.
        category_group (pygame.sprite.Group): Group for managing category buttons.
        level_group (pygame.sprite.Group): Group for managing level buttons.
        selected_category (RadioButton): The currently selected category button.
        selected_level (RadioButton): The currently selected level button.

    Methods:
        on_home(): Handles the click event for the home button.
        on_next(): Handles the click event for the next button, proceeding only if both category and level are selected.
        handle_events(): Handles events like button clicks and quitting.
        draw(): Draws the elements of the dashboard onto the screen.
        run(): The main loop that runs the dashboard.
    """

    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Corbel', 24)
        self.big_font = pygame.font.SysFont('Corbel', 36)
        self.bg_color = (255, 255, 255)
        self.text_color = (0,0,0)

        self.category_mapping = {
            "Math": "math",
            "Social Sciences": "social_sciences",
            "Science": "science"
        }

        # Define texts
        self.header_text = self.big_font.render('Debugger Dashboard', True, (0,0,0))
        self.subheader_text = self.font.render('Select a Category and Level to view all the questions', True, (0, 0, 0))
        
        # Define buttons
        self.home_button = GameScreenButtons(20, 20, 100, 40, 'Home', self.on_home)
        self.next_button = GameScreenButtons(screen.get_width() - 120, screen.get_height() - 60, 100, 40, 'Next', self.on_next)
        
        # Create radio buttons for categories
        self.category_buttons = [
            RadioButton(50, 200, 200, 50, self.font, "Math"),
            RadioButton(260, 200, 200, 50, self.font, "Social Sciences"),
            RadioButton(470, 200, 200, 50, self.font, "Science")
        ]
        
        # Create radio buttons for levels
        self.level_buttons = [
            RadioButton(50, 300, 50, 50, self.font, "1"),
            RadioButton(110, 300, 50, 50, self.font, "2"),
            RadioButton(170, 300, 50, 50, self.font, "3")
        ]

        # Horizontal centering for buttons
        total_categories_width = (200 + 10) * len(self.category_buttons) - 10  # 200px width per button, 10px spacing
        total_levels_width = (50 + 10) * len(self.level_buttons) - 10  # 50px width per button, 10px spacing
        
        # Starting x positions for centered buttons
        start_x_categories = (screen.get_width() - total_categories_width) // 2
        start_x_levels = (screen.get_width() - total_levels_width) // 2

        # Update x positions of buttons to center them
        for i, button in enumerate(self.category_buttons):
            button.rect.x = start_x_categories + i * (200 + 10)  # 200px width + 10px spacing
        for i, button in enumerate(self.level_buttons):
            button.rect.x = start_x_levels + i * (50 + 10)  # 50px width + 10px spacing

        # Labels for Category and Level - left-aligned
        label_offset_x = 10  # Offset from the left edge of the screen
        self.category_label_pos = (label_offset_x, 180)
        self.level_label_pos = (label_offset_x, 280)

        # Create the label surfaces
        self.category_label = self.font.render('Category', True, self.text_color)
        self.level_label = self.font.render('Level', True, self.text_color)

        # Set the first category and level as selected by default
        self.selected_category = None
        self.selected_level = None

        # Set up groups for update/draw calls
        self.category_group = pygame.sprite.Group(self.category_buttons)
        self.level_group = pygame.sprite.Group(self.level_buttons)
        
        # Set the radio button groups for mutual exclusivity
        for btn in self.category_buttons:
            btn.setRadioButtons(self.category_buttons)
        for btn in self.level_buttons:
            btn.setRadioButtons(self.level_buttons)

    def on_home(self):
        # ADD LOGIC
        print("Home button clicked")


    def on_next(self):
        # Only proceed if both a category and a level are selected
        if self.selected_category and self.selected_level:
            # Map the selected category's text to the corresponding key in the JSON file
            category_key = self.category_mapping.get(self.selected_category.text, "").lower()
            level_key = f"level{self.selected_level.text}"
            debugger_mode_screen = DebuggerModeScreen(self.screen, category_key, level_key)
            debugger_mode_screen.run()

    def handle_events(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            self.home_button.handle_event(event)
            # The next button is only active if both a category and level are selected
            if self.selected_category and self.selected_level:
                self.next_button.handle_event(event)

            # Update the radio buttons and check selections
            self.category_group.update(event_list)
            self.level_group.update(event_list)
            for button in self.category_buttons:
                if button.clicked:
                    self.selected_category = button
            for button in self.level_buttons:
                if button.clicked:
                    self.selected_level = button


    def draw(self):
        self.screen.fill(self.bg_color)

        # Draw header and sub-header
        self.screen.blit(self.header_text, (self.screen.get_width() // 2 - self.header_text.get_width() // 2, 20))
        self.screen.blit(self.subheader_text, (self.screen.get_width() // 2 - self.subheader_text.get_width() // 2, 80))

        # Draw "Category" and "Level" labels
        self.screen.blit(self.category_label, self.category_label_pos)
        self.screen.blit(self.level_label, self.level_label_pos)

        # Draw buttons
        self.home_button.draw(self.screen)
        if self.selected_category and self.selected_level:
            self.next_button.draw(self.screen)

        # Draw radio buttons
        self.category_group.draw(self.screen)
        self.level_group.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.draw()
            self.clock.tick(60)


class DebuggerModeScreen:
    """
    This class represents the screen where the debugger mode is active.
    It displays all questions and answers based on the selected category and level.
    """
    def __init__(self, screen, category, level):
        self.screen = screen
        self.category = category
        self.level = level
        self.load_questions()

    def load_questions(self):
        # Load the questions from the testbank.json file based on selected category and level
        testbank_path = os.path.join(src_dir, 'testbank.json')  # Ensure this path is correct
        with open(testbank_path, 'r', encoding='utf-8') as file:
            test_bank = json.load(file)
        self.questions = test_bank['subjects'].get(self.category, {}).get(self.level, [])

    def draw(self):
        # Code to draw the questions and answers
        pass

    def run(self):
        # The main loop for the debugger mode screen
        pass





# Example usage
# if __name__ == "__main__":
#     pygame.init()
#     screen = pygame.display.set_mode((844, 600))
#     dashboard_page = DebuggerDashboardPage(screen)
#     dashboard_page.run()
    
# Example usage
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((844, 600))
    dashboard_page = DebuggerDashboardPage(screen)

    # Simulate user selecting "Math" and "Level 1"
    dashboard_page.selected_category = dashboard_page.category_buttons[0]  # Assuming this is "Math"
    dashboard_page.selected_level = dashboard_page.level_buttons[0]  # Assuming this is "Level 1"

    # Normally, user clicks "Next" and triggers on_next()
    # For this example, we'll call on_next() directly to simulate this action
    dashboard_page.on_next()

    # This would normally not return until the DebuggerModeScreen is closed
    dashboard_page.run()