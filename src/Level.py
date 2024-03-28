# @author Harjap

import json
import random
from question2 import Question
import os

class Level:
    
    # Constructor to create a level
    # @param lvlNum, the level number
    def __init__(self, lvlNum, catagory):
        self.levelNum = lvlNum
        self.playerHPThreshold = 100

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

    

