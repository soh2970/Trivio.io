import unittest
from question2 import Question
from Player import Player
from Instructor import Instructor

q = Question(1, "Hello", [1,2,3,4], 4, 69, False, "Math")
player = Player(1, 0, 0, 1)
instructor = Instructor()

"""
Tests if the Player class method answerQuestion works
"""
class TestPlayerClass(unittest.TestCase):
    def testAnswerQuestion(self):
        result = player.answerQuestion(q, 4)
        self.assertEqual(result, True)


class TestInstructorClass(unittest.TestCase):

    def testGetPlayerStats(self):
        print(instructor.getPlayerStats("natetyu"))
