# @author Harjap

import json
import random

class Level:

    # private varaibles for the levels number,hp threasholds, and questions
    levelNum
    playerHPThreshold
    bossHPThreshold
    questionsInLevel
    usedQuestions
    
    # Constructor to create a level
    # @param lvlNum, the level number
    def __init__(self, lvlNum, catagory):
        self.levelNum = lvlNum
        self.playerHPThreshold = 0

        if( lvlNum == 1){ self.bossHPThreshold = 80}
        else if (lvlNum == 2){self.bossHPThreshold = 50}
        else {self.bossHPThreshold = 0}

        self.questionsInLevel = getQuestions(lvlNum, catagory) 
        self.usedQuestions = []
    
    # Method to get all the questions in a certain level and catagory
    # @param level, the level number
    # @param catagory, the level catagory
    # @return a list of all question with the given level and catagory
    def getQuestions(level, catagory):
        with open('data.json') as f:
            json_data = json.load(f)
        questions = json_data['questions']
        qList = []
        for i in questions:
            if (i['catagory'] == catagory && (i['level'] == level)){ qList.append(i)}
        
        return qList

    
    # Method to check if a level is complete
    # @param playerHp, the player's hp
    # @param bossHp, the bosses hp
    # @return boolean, true if level is completed and false if not
    def completeLevel(playerHp, bossHp):
        if ((playerHp > self.playerHPThreshold) && (bossHp <= self.bossHPThreshold)){return True}
        else {return False}
    
    # Method to get the next question
    # @return the next question
    def getNextQuestion():
        # get a random question
         q = random.choice(self.questionsInLevel)

         # if there are no used questions then append the question to usedq and return q
         if len(self.usedQuestions) 0{
            self.usedQuestions.append(q)
            return q
         }
         else{ # if there are used questions then get a question that is not used and append it then return it
            while(q in self.usedQuestions){
                q = random.choice(self.questionsInLevel)
            }

            self.usedQuestions.append(q)
            return q
         }

    


