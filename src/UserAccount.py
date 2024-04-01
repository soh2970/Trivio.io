import json
import os

class UserAccount:
    """
    Handles user account creation, validation, and management within the game, storing user data in a JSON file.

    Attributes:
        ID (str): The user ID, which is converted to lowercase to ensure case-insensitive login.
        password (str): The user's password.

    Methods:
        __init__(self, userID, userPassword):
            Initializes a new user account with the provided ID and password.

        validateLogin(self):
            Validates the user's login attempt by checking the provided credentials against the stored data.
            Returns True if the login is successful, False otherwise.

        createAccount(self):
            Creates a new user account with the provided ID and password. If the user ID already exists in the data store,
            raises a UserFoundException indicating that the user cannot be created because it already exists.

            User data includes a default saved game state and an initial high score of 0. The method updates the JSON data store
            with the new user information.
    """
    
    def __init__(self, userID, userPassword):
        self.ID = userID.lower()
        self.password = userPassword

    def validateLogin(self):
        base_dir = os.path.dirname(__file__)  # Get the directory where UserAccount.py is located
        json_path = os.path.join(base_dir, 'playerBank.json')

        with open(json_path, "r") as file:
            data = json.load(file)
            if self.ID in data:
                if self.password == data[self.ID]["password"]:
                    return True
        return False
    
    def createAccount(self):

        name = self.ID
        password = self.password

        playerData = {
            "password": password,
            "currentSavedGame": {},
            "highscore": 0
        }

        base_dir = os.path.dirname(__file__)  # Get the directory where UserAccount.py is located
        json_path = os.path.join(base_dir, 'playerBank.json')
        
        with open(json_path, "r+") as file:
            data = json.load(file)
            if name not in data:
                data[name] = playerData
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
            else: raise UserFoundException("Player already found in database")




    