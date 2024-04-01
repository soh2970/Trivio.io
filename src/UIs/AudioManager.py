"""
will be used to manage the music in the background of the gameplay
"""
import pygame

class AudioManager:
    """
    Manages background music playback for a game, utilizing pygame for music control.
    Allows for loading songs, playing them on a loop, stopping playback, navigating between
    tracks, and adjusting volume.

    Attributes:
        songs (list of dict): A list of dictionaries where each dictionary contains 'name'
            and 'path' keys for song names and their respective file paths.
        current_song_index (int): The index of the currently loaded song in the songs list,
            used to keep track of which song is playing.

    Methods:
        __init__(self):
            Initializes the AudioManager instance, sets up the pygame mixer, sets the initial
            volume to 50%, and loads the default song.

        load_song(self, index):
            Loads a song based on the provided index from the songs list into the pygame mixer.

        play_song(self):
            Plays the currently loaded song on a loop indefinitely until stopped or changed.

        stop_song(self):
            Stops the music playback immediately.

        next_song(self):
            Advances to the next song in the list, automatically wraps to the first song if
            currently at the last song, and plays the selected song.

        prev_song(self):
            Moves to the previous song in the list, automatically wraps to the last song if
            currently at the first song, and plays the selected song.

        set_volume(self, volume):
            Sets the volume for music playback. The volume should be a float between 0.0 and 1.0,
            where 0.0 is silent and 1.0 is the maximum volume.

        get_current_song_name(self):
            Returns the name of the currently playing song.
    """
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