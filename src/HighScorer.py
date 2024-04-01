# @author Harjap

import json
import os

class HighScore():

    # constructor to get the highScore list
    def __init__(self):
        base_dir = os.path.dirname(__file__)  # Get the directory where Level.py is located
        json_path = os.path.join(base_dir, 'playerBank.json')

        with open(json_path, encoding='utf-8') as f:
            self.json_data = json.load(f)
        
        self.rankList = self.json_data.items()
        self.rankList = sorted(self.rankList, key=lambda x: x[1]['highscore'], reverse = True)
    
    # getter for highScores
    # @return highScores
    def getScoresDict(self):
        return self.json_data
    
    # get a player's game info
    # @param playerName, name of player
    # return the player's game info
    def getPlayerGameInfo(self, playerName):
        return self.json_data[playerName]['currentSavedGame']

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
    



