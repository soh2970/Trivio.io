class GameSetting:
    """
    Manages the game settings, including sound preferences and screen resolution.

    Attributes:
        sound (bool): Indicates whether sound is enabled (True) or disabled (False).
        screenResolution (tuple): The current screen resolution as a tuple (width, height).

    Methods:
        __init__(self, sound=True, screenResolutions=(844, 600)):
            Initializes the GameSetting object with default or specified sound settings and screen resolution.

        toggleSound(self):
            Toggles the sound setting between on and off.

        setScreenResolution(self, width, height):
            Sets the screen resolution to the specified width and height.

        getSoundStatus(self):
            Returns the current sound setting (True for on, False for off).

        getScreenResolutions(self):
            Returns the current screen resolution as a tuple (width, height).
    """
    
    def __init__(self, sound=True, screenResolutions=(844,600)):
        self.sound = sound
        self.screenResolution = screenResolutions

    def toggleSound(self):
        self.sound = not self.sound

    def setScreenResolution(self, width, height):
        self.screenResolution = (width, height)

    def getSoundStatus(self):
        return self.sound
    
    def getScreenResolutions(self):
        return self.screenResolution