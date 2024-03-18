import random
import json
from Player import Player
from question2 import Question
import datetime
from Boss import Boss

class Game:
    def __init__(self):
        self.player = None
        self.currentLevel = 1
        self.testBank = self.load_test_bank()
        self.currentCategory = None
        self.currentQuestions = []
        self.gameState = "NotStarted"
        self.boss = Boss()  # Initialize boss object

    def load_test_bank(self):
        with open('testbank.json', 'r') as file:
            return json.load(file)
        
    def selectCategory(self, category):
        self.currentCategory = category
        if category in self.testBank['subjects']:
            self.currentQuestions = self.testBank['subjects'][category]['level' + str(self.currentLevel)]
        else:
            raise ValueError("Selected category doesn't exist")
        
    def startGame(self, playerId):
        self.player = Player(playerId, 100, 0, self.currentLevel)
        self.gameState = "InProgress"

    def presentQuestion(self):
        if self.currentQuestions:
            questionData = random.choice(self.currentQuestions)
            question = Question(questionData['questionID'], questionData['question'],
                                questionData['options'], questionData['correctAnswer'],
                                questionWeight=1, answeredCorrectly=False,
                                category=self.currentCategory)
            return question
        else:
            raise Exception("No questions available for current level & category")
        
    def answerQuestion(self, question, answer):
        if self.player.answerQuestion(question, answer):
            self.player.incrementScore()
        else:
            self.player.losePlayerHP()
        
        if self.player.isPlayerDefeated():
            self.endGame()

    def calculateScore(self):
        score = 0
        for question in self.player.questionsAnsweredCorrectly:
            score += question.questionWeight * self.currentLevel
        return score

    def nextLevel(self):
        if self.currentLevel < 3:
            self.currentLevel += 1
            self.player.moveToNextLevel(self.currentLevel)
            self.selectCategory(self.currentCategory)
        else:
            self.gameState = "BossFight"

    def bossFight(self):
        if not self.boss.isBossDefeated():
            self.player.losePlayerHP()  # Simulate player losing HP in boss fight
            self.boss.loseBossHP(self.currentLevel)  # Boss loses HP based on current level
            if self.player.isPlayerDefeated() or self.boss.isBossDefeated():
                self.endGame()

    def endGame(self):
        self.gameState = "Completed"
        self.saveGame()

    def saveGame(self):
        game_state = {
            'timeStamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'levelAchieved': self.player.currentLevel,
            'subject': self.current_category,
            'score': self.calculateScore()  # Update to use calculateScore method
        }
        
        with open('playerBank.json', 'r+') as file:
            player_bank = json.load(file)
            player_id = self.player.playerId

            if player_id in player_bank:
                player_bank[player_id]['gameHistory'].append(game_state)
                player_bank[player_id]['currentSavedGame'] = game_state
            else:
                pass
            file.seek(0)
            json.dump(player_bank, file, indent=4)
            file.truncate()

    def loadGame(self):
        with open('playerBank.json', 'r') as file:
            playerBank = json.load(file)
            playerId = self.player.playerId

            if playerId in playerBank and 'currentSavedGame' in playerBank[playerId]:
                savedGame = playerBank[playerId]['currentSavedGame']
                self.currentLevel = int(savedGame['levelAchieved'])
                self.currentCategory = int(savedGame['subject'])
                self.player.playerScore = int(savedGame['score'])
                self.gameState = "Loaded"
            else:
                print("No saved game for player: ", playerId)

    def exitToMainMenu(self):
        print("Exiting to main menu")
        #to be implemented, but for example
        mainMenu = MainMenu()
        mainMenu.show()