import random
import json
from Player import Player
from question2 import Question
import datetime
from Boss import Boss
from MainMenu import MainMenu
import pygame

pygame.init()

class Game:
    """
    Class representing the game engine for Trivio.

    Attributes:
        player (Player): The current player.
        currentLevel (int): The current level of the game.
        testBank (dict): The dictionary containing test bank questions.
        currentCategory (str): The current category of questions.
        currentQuestions (list): The list of current questions.
        gameState (str): The current state of the game.
        boss (Boss): The boss object for boss fights.
    """

    def __init__(self):
        """
        Initializes the Game object.
        """
        self.player = None
        self.currentLevel = 1
        self.testBank = self.load_test_bank()
        self.currentCategory = None
        self.currentQuestions = []
        self.gameState = "NotStarted"
        self.boss = Boss()

    def load_test_bank(self):
        """
        Loads the test bank questions from 'testbank.json'.

        Returns:
            dict: A dictionary containing the test bank questions.
        """
        #please alter the file path with your local directory of where testbank.json is located at
        with open("C:/Users/kimgu/2212/repositories2212/personalRepo2212/src/testbank.json",
                'r', encoding='utf-8') as file:
            return json.load(file)
        
    def selectCategory(self, category):
        """
        Selects the category of questions for the game.

        Args:
            category (str): The category of questions to select.
        
        Raises:
            ValueError: If the selected category doesn't exist in the test bank.
        """
        self.currentCategory = category
        if category in self.testBank['subjects']:
            self.currentQuestions = self.testBank['subjects'][category]['level' + str(self.currentLevel)]
        else:
            raise ValueError("Selected category doesn't exist")
        
    def startGame(self, playerId):
        """
        Starts a new game session for the specified player.

        Args:
            playerId (str): The ID of the player starting the game.
        """
        self.player = Player(playerId, 100, 0, self.currentLevel)
        self.gameState = "InProgress"

    def presentQuestion(self):
        """
        Presents a question to the player.

        Returns:
            Question: A Question object representing the presented question.

        Raises:
            Exception: If no questions are available for the current level and category.
        """
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
        """
        Processes the player's answer to a question.

        Args:
            question (Question): The question being answered.
            answer: The player's answer to the question.
        """
        if self.player.answerQuestion(question, answer):
            self.player.incrementScore()
        else:
            self.player.losePlayerHP()
        
        if self.player.isPlayerDefeated():
            self.endGame()

    def calculateScore(self):
        """
        Calculates the player's score based on the questions answered correctly.

        Returns:
            int: The player's score.
        """
        score = 0
        for question in self.player.questionsAnsweredCorrectly:
            # Adjust score calculation based on the player's current level
            if self.player.currentLevel == 1:
                score += question.questionWeight * 1
            elif self.player.currentLevel == 2:
                score += question.questionWeight * 2
            elif self.player.currentLevel == 3:
                score += question.questionWeight * 3
        return score

    def nextLevel(self):
        """
        Advances the game to the next level.
        """
        if self.currentLevel < 3:
            self.currentLevel += 1
            self.player.moveToNextLevel(self.currentLevel)
            self.selectCategory(self.currentCategory)
        else:
            self.gameState = "BossFight"

    def bossFight(self):
        """
        Simulates a boss fight scenario in the game.
        """
        if not self.boss.isBossDefeated():
            self.player.losePlayerHP()
            self.boss.loseBossHP(self.currentLevel)
            if self.player.isPlayerDefeated() or self.boss.isBossDefeated():
                self.endGame()

    def endGame(self):
        """
        Ends the current game session.
        """
        self.gameState = "Completed"
        self.saveGame()

    def saveGame(self):
        """
        Saves the game state to the player bank.
        """
        game_state = {
            'timeStamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'levelAchieved': self.player.currentLevel,
            'subject': self.currentCategory,
            'score': self.calculateScore()
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
        """
        Loads a saved game state from the player bank.
        """
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
        """
        Exits the current game session and returns to the main menu.
        """
        print("Exiting to main menu")
        #to be implemented, but for example
        mainMenu = MainMenu()
        mainMenu.show()


if __name__ == "__main__":
    game = Game()
    main_menu = MainMenu(game)
    main_menu.run()