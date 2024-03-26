"""
will be used to manage the music in the background of the gameplay
"""
import pygame

class AudioManager:
    def __init__(self, background_music_path):
        pygame.mixer.init()
        self.songs = [
            {'name': '', 'path': '', }
        ]
        self.current_song_index = 0
        self.load_song(self.current_song_index)
        # default volume set at 50%
        self.volume = 0.5 
    
    
    def load_song(self, index):
        pygame.mixer.music.load(self.songs[index]['path'])
        pygame.mixer.music.set_volume(self.volume)
    
    def play_song(self):
        pygame.mixer.music.play(-1)
    
    def stop_song(self):
        pygame.mixer.music.stop()

    def next_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.songs)
        self.load_song(self.current_song_index)
        self.play_song()

    def prev_song(self):
        self.current_song_index = (self.current_song_index - 1) % len(self.songs)
        self.load_song(self.current_song_index)
        self.play_song()
    
    def set_volume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(volume)
    
    def get_current_song_name(self):
        return self.songs[self.current_song_index]['name']