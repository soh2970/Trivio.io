# @author Harjap

import json
import random
from question2 import Question
import os

class Level:
    """
    Represents a level in the game, including managing the questions for the level, 
    checking level completion, and handling level progression.

    Attributes:
        levelNum (int): The current level number.
        playerHPThreshold (int): The HP threshold for the player. Set to 100 by default.
        catagory (str): The category of questions for the current level.
        bossHPThreshold (int): The HP threshold that the boss must be reduced to in order to complete the level.
        questionWeight (int): The weight or value of questions in this level.
        questionsInLevel (list): A list of Question objects available in this level.
        usedQuestions (list): A list of questions that have already been used in the current level to avoid repetition.

    Methods:
        __init__(lvlNum, catagory):
            Initializes a new level with the given level number and category. Sets the playerHPThreshold, 
            bossHPThreshold, questionWeight, and loads the questions for the level.

        getQuestions(level, catagory):
            Loads questions for the specified level and category from the 'testbank.json' file.

            Args:
                level (int): The level number.
                catagory (str): The category of questions.

            Returns:
                list: A list of Question objects for the level and category.

        completeLevel(playerHp, bossHp):
            Checks whether the level is complete based on the player's HP and the boss's HP.

            Args:
                playerHp (int): The current HP of the player.
                bossHp (int): The current HP of the boss.

            Returns:
                bool: True if the level is completed, False otherwise.

        moveToNextLevel(level):
            Updates the level object to the next level, loading new questions for the specified level.

            Args:
                level (int): The next level number.

        getNextQuestion():
            Selects and returns the next question for the player from the list of unused questions.

            Returns:
                Question: The next question object.
    """
    # Constructor to create a level
    # @param lvlNum, the level number
    def __init__(self, lvlNum, catagory):
        self.levelNum = lvlNum
        self.playerHPThreshold = 100
        self.catagory = catagory

        if( lvlNum == 1): 
            self.bossHPThreshold = 80 
            self.questionWeight = 4  
        elif (lvlNum == 2): 
            self.bossHPThreshold = 50
            self.questionWeight = 6
        else: 
            self.bossHPThreshold = 0
            self.questionWeight = 10

        self.questionsInLevel = self.getQuestions(lvlNum, catagory) 
        self.usedQuestions = []
    
    # Method to get all the questions in a certain level and catagory
    # @param level, the level number
    # @param catagory, the level catagory
    # @return a list of all question with the given level and catagory
    def getQuestions(self, level, catagory):
        base_dir = os.path.dirname(__file__)  # Get the directory where Level.py is located
        json_path = os.path.join(base_dir, 'testbank.json')

        with open(json_path, encoding='utf-8') as f:
            json_data = json.load(f)
            subjects = json_data['subjects']
            qList = []
            if catagory in subjects:
                catagoryData = subjects[catagory]
                levelKey = f'level{level}'
                if levelKey in catagoryData:
                # Access the questions for the specific level
                    for question in catagoryData[levelKey]:
                        q = Question(question['question'], question['options'], question['correctAnswer'], self.questionWeight, catagory)
                        qList.append(q)
            return qList
    
    # Method to check if a level is complete
    # @param playerHp, the player's hp
    # @param bossHp, the bosses hp
    # @return boolean, true if level is completed and false if not
    def completeLevel(self, playerHp, bossHp):
        return playerHp > self.playerHPThreshold and bossHp <= self.bossHPThreshold
    
    def moveToNextLevel(self, level):
        self.questionsInLevel = self.getQuestions(level, self.catagory)
        self.levelNum = level

    
    # Method to get the next question
    # @return the next question
    def getNextQuestion(self):
        # get a random question
        q = random.choice(self.questionsInLevel)

         # if there are no used questions then append the question to usedq and return q
        if len(self.usedQuestions) > 0:
            while q in self.usedQuestions:
                random.shuffle(self.questionsInLevel)
                q = self.questionsInLevel[0]

         
        self.usedQuestions.append(q)
        return q

    

