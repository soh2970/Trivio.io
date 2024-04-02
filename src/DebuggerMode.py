from question2 import Question
import json
import os

print(os.listdir())

class Debugger:
    """
    Provides functionalities for debugging and testing questions from the game's question bank.
    Allows selection of a specific question based on category, level, and question number to test or debug.

    Attributes:
        password (int): A hardcoded password to access debugging functionalities.

    Methods:
        __init__(self): 
            Initializes the Debugger object.

        selectQuestion(self, category, level, questionNum):
            Selects and returns a Question object based on the specified category, level, and question number. 
            It reads from a JSON file containing the question bank, constructs a Question object with the retrieved 
            data, and returns it.

            Parameters:
                category (str): The category of the question (e.g., 'math', 'social_sciences', 'science').
                level (int): The difficulty level of the question (1 to 3).
                questionNum (int): The index of the question in the question bank for the specified category and level.

            Returns:
                Question: An instance of the Question class populated with the data of the selected question.
    """

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
