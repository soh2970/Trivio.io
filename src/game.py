import pygame
import sys

class Game: 
    def __init__(self):
        pygame.init()

        #display setter
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Trivio")

        #game state variables
        self.running = True
        self.current_level = None
        self.player = None 

        #load resources
        self.load_resources()
        self.state = "MainMenu"

    def load_resources(self):
        #load images, sourds, other resources
        pass

    def start_new_game(self): 
        #setup new game

        #create new player instance, load levels, etc
        self.player = Player("Player A") #pass
        self.current_level = Level(1) #level class
        self.state = "Playing"

    def load_game(self):
        #load a saved game state
        pass

    def save_game(self):
        #implement game saving logic
        pass

    def main_menu(self):
        #display the main menu
        #rendering & handling menu selections
        pass

    def handle_events(self):
        #handle keyboard & mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            #other input handlings
                
    def update(self):
        #update game state
        if self.state == "Playing":
            #update current lvl, player state, etc
            pass
        elif self.state ==  "MainMenu":
            self.main_menu()

    def render(self):
        #render current state to screen
        self.screen.fill((0,0,0)) #alter, depending on UI/UX
        if self.state == "Playing":
            #render game level
            pass
        #add more rendering for diff states

        #update display
        pygame.display.flip()

    def run(self):
        #main game loop
        while self.running:
            self.handle_events()
            self.update()
            self.render()

        self.quit()

    def quit(self):
        #quit game
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()