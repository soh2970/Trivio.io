class GameSetting:
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