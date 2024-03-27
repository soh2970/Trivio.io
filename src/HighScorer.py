# @author Harjap

import json

class HighScore():

    # constructor to get the highScore list
    def __init__(self):
        with open('playerBank.json') as f:
            self.json_data = json.load(f)
            print(type(self.json_data))
            print(self.json_data.keys())
           
    
    # getter for highScores
    # @return highScores
    def getScoresDict(self):
        return self.json_data
    
    # get a player's score
    # @param playerName, name of player whose score is wanted
    # @return 0 if there is no such player, otherwise return the player's score
    def getPlayerScore(self, playerName):
        return self.json_data[playerName]["score"]

    # check if the given player has a score.
    # @param playerName, name of the player who we want to check.
    # @return True if player has a score and false if not.
    def checkForScore(self, playerName):
        if playerName in self.json_data:
            return True    
        else: 
            return False
    
    def top3(self):
        first = ''
        second = ''
        third = ''
        for i in self.json_data.keys():
            if (third == ''):
                third = first = second = i
            
            else:
                if (self.json_data[first]['score'] < self.json_data[i]['score']):
                    third = second
                    second = first
                    first = i
                elif(self.json_data[second]['score'] < self.json_data[i]['score']):
                    third = second
                    second = i
                elif(self.json_data[third]['score'] < self.json_data[i]['score']):
                    third = i
        return [[first, self.json_data[first]['score']]]



