class Player:
    """
    Represents a player in the game, holding player-specific data such as ID, health points (HP),
    score, and the current level the player is on. Provides methods to manage the player's state
    and actions within the game.

    Attributes:
        playerId (str): A unique identifier for the player.
        playerHP (int): The player's current health points.
        playerScore (int): The player's current score.
        currentLevel (int): The current level the player is on.

    Methods:
        answerQuestion(self, question, answer):
            Determines if the provided answer to a question is correct, affecting the game state.

        losePlayerHP(self, level):
            Deducts health points from the player based on the difficulty level of a question.

        isPlayerDefeated(self):
            Checks if the player's health points have dropped to zero or below.

        incrementScore(self):
            Increases the player's score based on the difficulty level of a correctly answered question.

        moveToNextLevel(self, level):
            Advances the player to the specified level, with validation to ensure it's within an acceptable range.
    """

    def __init__(self, playerId, playerHP, playerScore, currentLevel):
        self.playerId = playerId
        self.playerHP = playerHP
        self.playerScore = playerScore
        self.currentLevel = currentLevel

    def answerQuestion(self, question, answer):
        return question.checkAnswer(answer)

    def losePlayerHP(self, level):
        if (level == 1):
            self.playerHP = self.playerHP - 4
        elif (level == 2):
            self.playerHP = self.playerHP - 6
        elif (level == 3):
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
        else:
            raise Exception("Level not in range from 1-3")