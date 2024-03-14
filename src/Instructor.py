import json

class Instructor: 
    password = "1234567890"

    def __init__(self):
        pass

    def searchPlayerName(name):
        pass

    """
    Returns a list of previous completed games
    """
    def getPlayerStats(self, player):                                           
        with open('playerBank.json', 'r') as file:
            data = json.load(file)
            if player in data:
                return data[player]["gameHistory"]
            else: 
                raise Exception("Player not found")
