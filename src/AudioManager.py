"""
will be used to manage the music in the background of the gameplay
"""
import pygame


class AudioManager:
    def __init__(self, background_music_path):
        pygame.mixer.init()
        self.background_music_path = background_music_path
        # default volume set at 50%
        self.volume = 0.5 
    
    def play_background_music(self):
        pygame.mixer.music.load(self.background_music_path)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)
    
    def set_volume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(volume)