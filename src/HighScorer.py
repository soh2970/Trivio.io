# @author Harjap

import json
import os

class HighScore():
    """
    Manages high scores for a game, loading player scores from a JSON file and providing functionality
    to retrieve and sort these scores.

    Attributes:
        json_data (dict): The loaded JSON data containing player scores and information.
        rankList (list): A sorted list of players and their scores, from highest to lowest.

    Methods:
        __init__(self):
            Initializes the HighScore object by loading player scores from 'playerBank.json' and
            sorting them into rankList based on high scores in descending order.

        getScoresDict(self):
            Returns the complete dictionary of player scores and information as loaded from JSON.

        getPlayerGameInfo(self, playerName):
            Retrieves the saved game information for a specified player.
            Parameters:
                playerName (str): The name of the player whose game information is to be retrieved.
            Returns:
                dict: The game information for the specified player.

        checkForScore(self, playerName):
            Checks if a specified player has a saved score.
            Parameters:
                playerName (str): The name of the player to check for a saved score.
            Returns:
                bool: True if the player has a saved score, False otherwise.

        scoreRankings(self):
            Returns a sorted list of players and their high scores, from highest to lowest.
    """
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
    



