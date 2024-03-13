class Player:

    def __init__(self, playerId, playerHP, playerScore, currentLevel):
        self.playerId = playerId
        self.playerHP = playerHP
        self.playerScore = playerScore
        self.currentLevel = currentLevel

    def answerQuestion(self, question, answer):
        return question.checkAnswer(answer)

    def losePlayerHP(self):                                                                              
        if (self.currentLevel == 1):
            self.playerHP = self.playerHP - 4
        elif (self.currentLevel == 2):
            self.playerHP = self.playerHP - 6
        elif (self.currentLevel == 3): 
            self.playerHP = self.playerHP - 10

    def isPlayerDefeated(self):
        if (self.playerHP <= 0):
            return True
        else: return False

    def incrementScore(self):
        if (self.currentLevel == 1):
            self.playerScore = self.playerScore + 4
        elif (self.currentLevel == 2):
            self.playerScore = self.playerScore + 6
        elif (self.currentLevel == 3):
            self.playerScore = self.playerScore + 10

    def moveToNextLevel(self, level):
        if (level <= 3 and level > 0):
            self.currentLevel = level
        else: raise Exception("Level not in range from 1-3")


