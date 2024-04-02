import json

class Instructor: 
    """
    Represents an instructor role within the game, allowing access to view player statistics.

    Attributes:
        password (str): The password required for instructor access. Set to "1234567890" by default.

    Methods:
        __init__(): Initializes an Instructor instance. Currently, it does not require any parameters and performs no actions.
        getPlayerStats(player):
            Retrieves the game history for a specified player from the 'playerBank.json' file.

            Args:
                player (str): The ID of the player whose stats are being requested.

            Returns:
                list: A list containing the history of games played by the player, including scores and dates.

            Raises:
                Exception: If the specified player is not found in the 'playerBank.json' file.
    """
    password = "1234567890"

    def __init__(self):
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

    