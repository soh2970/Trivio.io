# @author Harjap

import json

class HighScore:

    # constructor to get the highScore list
    def __init__(self):
        with open('players.json') as f:
            json_data = json.load(f)
        p = json_data['players']
        self.highScores = p.sort(key = 'score', reversed = True)
    
    # getter for highScores
    # @return highScores
    def getScoresList(self):
        return self.highScores
    
    # get a player's score
    # @param playerName, name of player whose score is wanted
    # @return 0 if there is no such player, otherwise return the player's score
    def getPlayerScore(self, playerName):
        for i in self.highScores:
            if (i.userName == playerName):
                return i.score
        return 0

    # check if the given player has a score.
    # @param playerName, name of the player who we want to check.
    # @return True if player has a score and false if not.
    def checkForScore(self, playerName):
        for i in self.highScores:
               if (i.userName == playerName):
                return True    
        return False




