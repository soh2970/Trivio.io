import io
import pygame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

class Question:
    def __init__(self, prompt, options, correct_option, is_latex=False):
        self.prompt = prompt
        self.options = options
        self.correct_option = correct_option
        self.is_latex = is_latex
        self.rendered_prompt = None
        self.rendered_options = []

        if self.is_latex:
            self.render_latex()
        else:
            self.render_text()

    def render_text():
        pass

    def render_latex(self):
        # Render LaTeX string to an image
        self.rendered_prompt = self.latex_to_image(self.prompt)
        for option in self.options:
            rendered_option = self.latex_to_image(option)
            self.rendered_options.append(rendered_option)

    def latex_to_image(self, latex_str):
        # Render a LaTeX string to an image using Matplotlib
        fig = plt.figure()
        text = fig.text(0, 0, latex_str, fontsize=14, usetex=True)

        # Save the figure to a StringIO object to avoid writing to disk
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        plt.close(fig)

        # Load the image into Pygame
        buffer.seek(0)
        image = pygame.image.load(buffer)
        return image
    
    def is_correct(self, player_answer):
        return player_answer == self.correct_option
    
    def display(self, screen):
        if self.is_latex:
            screen.blit(self.rendered_prompt, (50, 50))
            for i, option_img in enumerate(self.rendered_options):
                screen.blit(option_img, (50, 100 + i*50))
        else:
            font = pygame.font.Font(None, 36)
            text_surface = font.render(self.prompt, True, (255, 255, 255))
            screen.blit(text_surface, (50, 50))
            for i, option in enumerate(self.options):
                option_surface = font.render(option, True, (255, 255, 255))
                screen.blit(option_surface, (50, 100 + i*50))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    latex_question = Question(
        r"\frac{1}{2} + \frac{3}{4}",
        [r"$\frac{5}{4}$", r"$\frac{1}{4}$", r"$\frac{2}{4}$", r"$1$"],
        0,
        is_latex=True
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black
        latex_question.display(screen)
        pygame.display.flip()

    pygame.quit()