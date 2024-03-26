"""
will be used to manage the music in the background of the gameplay
"""
import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.songs = [
            {'name': 'Default', 'path': 'audio/default_background_music.mp3'},
            {'name': 'Song 1', 'path': 'audio/song1_background_music.mp3'},
            {'name': 'Song 2', 'path': 'audio/song2_background_music.mp3'},
            {'name': 'Song 3', 'path': 'audio/song3_background_music.mp3'}
        ]
        self.current_song_index = 0
        
        # default volume set at 50%
        pygame.mixer.music.set_volume(0.5)

        self.load_song(self.current_song_index)
    
    
    def load_song(self, index):
        pygame.mixer.music.load(self.songs[index]['path'])
    
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
        pygame.mixer.music.set_volume(volume)
    
    def get_current_song_name(self):
        return self.songs[self.current_song_index]['name']