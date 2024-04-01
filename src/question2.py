class Question:
    """
    Represents a single quiz question, including its text, answer choices, correct answer, weight, and category.

    Attributes:
        prompt (str): The text of the question being asked.
        choices (list): A list of possible answers to the question.
        correctAnswer (str): The correct answer to the question.
        questionWeight (int): A value representing the difficulty or importance of the question.
        category (str): The category or subject area of the question.

    Methods:
        __init__(self, prompt, choices, correctAnswer, questionWeight, category):
            Initializes a new Question object with the provided question text, answer choices,
            correct answer, weight, and category.
    """
    def __init__(self, prompt, choices, correctAnswer, questionWeight, category):
        self.prompt = prompt
        self.choices = choices
        self.correctAnswer = correctAnswer
        self.questionWeight = questionWeight
        self.category = category
    



    
        
        

    
        
    