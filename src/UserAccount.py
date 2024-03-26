import json

class UserAccount:

    def __init__(self, userID, userPassword):
        self.ID = userID.lower()
        self.password = userPassword

    def validateLogin(self):
        with open("src/playerBank.json", "r") as file:
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
            "gameHistory" : [],
            "currentSavedGame": {}
        }

        with open("src/playerBank.json", "r+") as file:
            data = json.load(file)
            if name not in data:
                data[name] = playerData
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
            else: raise Exception("Player already found in database")




    