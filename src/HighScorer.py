# @author Harjap

import json

class HighScore():

    # constructor to get the highScore list
    def __init__(self):
        
        with open('playerBank.json') as f:
            self.json_data = json.load(f)
        
        self.rankList = self.json_data.items()
        self.rankList.sorted(self.rankList, key=lambda x: x[1]['currentSavedGame']['score'], reversed = True)


    
    # getter for highScores
    # @return highScores
    def getScoresDict(self):
        return self.json_data
    
    # get a player
    # @param playerName, name of player
    # return the player
    def getPlayerScore(self, playerName):
        return self.json_data[playerName]

    # check if the given player has a score.
    # @param playerName, name of the player who we want to check.
    # @return True if player has a score and false if not.
    def checkForScore(self, playerName):
        if playerName in self.json_data:
            return True    
        else: 
            return False
    
    def scoreRankings(self):
        return self.rankList



