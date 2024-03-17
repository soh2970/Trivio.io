# @author Harjap

import json
import random

class Level:
    
    # Constructor to create a level
    # @param lvlNum, the level number
    def __init__(self, lvlNum, catagory):
        self.levelNum = lvlNum
        self.playerHPThreshold = 100

        if( lvlNum == 1): 
            self.bossHPThreshold = 80

        elif (lvlNum == 2): 
            self.bossHPThreshold = 50
        else: 
            self.bossHPThreshold = 0

        self.questionsInLevel = self.getQuestions(lvlNum, catagory) 
        self.usedQuestions = []
    
    # Method to get all the questions in a certain level and catagory
    # @param level, the level number
    # @param catagory, the level catagory
    # @return a list of all question with the given level and catagory
    @staticmethod
    def getQuestions(level, catagory):
        with open('testbank.json') as f:
            json_data = json.load(f)
        questions = json_data['questions']
        qList = []
        for i in questions:
            if (i['catagory'] == catagory and (i['level'] == level)):
                qList.append(i)
        
        return qList

    
    # Method to check if a level is complete
    # @param playerHp, the player's hp
    # @param bossHp, the bosses hp
    # @return boolean, true if level is completed and false if not
    def completeLevel(playerHp, bossHp, ):
        return playerHp > self.playerHPThreshold and bossHp <= self.bossHPThreshold
    
    # Method to get the next question
    # @return the next question
    def getNextQuestion():
        # get a random question
        q = random.choice(self.questionsInLevel)

         # if there are no used questions then append the question to usedq and return q
        if len(self.usedQuestions) > 0:
            while q in self.usedQuestions:
                random.shuffle(self.questionsInLevel)
                q = self.questionsInLevel[0]

         
        self.usedQuestions.append(q)
        return q

    


