from question2 import Question
import json
import os

print(os.listdir())

class Debugger:

    password = 2468

    def __init__(self):
        pass

    
    def selectQuestion(self, category, level, questionNum):
        
        if (category == 'math') or (category == 'social_sciences') or (category == 'science'):
            if (level > 0) and (level <= 3):
                if (questionNum < 20) and (questionNum >= 0):
                    with open ("testbank.json", "r", encoding='utf-8') as file:
                        data = json.load(file)

                        levelNum = "level" + str(level)
                        prompt = data['subjects'][category][levelNum][questionNum]['question']
                        choices = data['subjects'][category][levelNum][questionNum]['options']
                        correctAnswer = data['subjects'][category][levelNum][questionNum]['correctAnswer']
                        
                        if (level == 1): questionWeight = 4
                        if (level == 2): questionWeight = 6
                        if (level == 3): questionWeight = 10

                        questionID = (questionNum, level)
                        return Question(questionID, prompt, choices, correctAnswer, questionWeight, category)
                    


debugTest = Debugger()
newQuestion = debugTest.selectQuestion('math', 1, 1)

print(newQuestion.questionID, newQuestion.prompt, newQuestion.choices, newQuestion.correctAnswer, newQuestion.questionWeight, newQuestion.answeredCorrectly, newQuestion.category)
