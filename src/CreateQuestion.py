import json

"""
This method will append you question to the testbank.json file. Make sure that you spell the categories and
levels exactly how they are layed out, or else the function will throw an error.

Please use this to create questions for the game, as it will be perfectly formatted in JSON and will take 
much less time to add question to the testbank.

If you need to delete a question, just manually remove it 
by going into the testbank and deleting the element in the associated level array. 

MAKE SURE THAT YOU RUN THIS SCRIPT IN THE SRC FOLDER OR ELSE PYTHON WILL THROW A FILE NOT FOUND ERROR.  

thanks :)
"""


def createQuestion():
    category = input("Enter the category of the question (math, geography, science (spell exactly))\n")
    level = input("Enter the level of the question (level1, level2, level3 (spell exactly))\n")
    prompt = input("Enter the question prompt\n")
    op1 = input("Enter 1st option (1/4)\n")
    op2 = input("Enter 2nd option (2/4)\n")
    op3 = input("Enter 3rd option (3/4)\n")
    op4 = input("Enter 4th option (4/4)\n")
    opArray = [op1,op2,op3,op4]
    correct = input("Now enter the correct answer (Must be the exact same string as one of the options.)\n")

    if (correct not in opArray):
        raise Exception("Correct answer did not match any of the previous option inputs\n")
    
    print("Confirm that these are the attributes of the question.\n" + "Category: " + category + "\nLevel: " + level + "\nPrompt: " + prompt + "\nOptions " + ", ".join(opArray) + "\nCorrect Answer: " + correct)
    response = input("Y for Yes, N for no (will exit function)\n")
    if (response.lower() == 'n'):
        return
    
    questionObject = {
        "question": prompt,
        "options": opArray,
        "correctAnswer": correct
    }

    writeQuestionToJson(questionObject, category, level)
    print("Question successfully added")
    
    response2 = input("Do you want to add another question (Y/N)\n")
    if (response2.lower() == 'n'):
        return
    elif (response2.lower() == 'y'):
        createQuestion()
    else:
        return

def writeQuestionToJson(newQuestion, category, level):
    with open("testbank.json", "r+") as testbank:
        file = json.load(testbank)
        file["subjects"][category][level].append(newQuestion)
        testbank.seek(0)
        json.dump(file, testbank, indent=4)
        testbank.truncate()

createQuestion()