class Question:
    def __init__(self, questionID, prompt, choices, correctAnswer, questionWeight, answeredCorrectly, category):
        self.questionID = questionID
        self.prompt = prompt
        self.choices = choices
        self.correctAnswer = correctAnswer
        self.questionWeight = questionWeight
        self.answeredCorrectly = answeredCorrectly
        self.category = category
    
    def checkAnswer(self, playerAnswer):
        self.answeredCorrectly = True if self.correctAnswer == playerAnswer else False
        return self.answeredCorrectly
    


q = Question(1, "Hello", [1,2,3,4], 4, 69, False, "Math")



    
        
        

    
        
    