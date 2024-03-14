import unittest
from question2 import Question
from Player import Player
from Instructor import Instructor
from unittest.mock import patch, MagicMock
from game import Game


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

#test cases for Game class
class TestGame(unittest.TestCase):
    @patch('Game.open', unittest.mock.mock_open(read_data='{"subjects": {"math": {"level1": [{"questionID": "1","question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "correctAnswer": "4"}]}}}'), create=True)
    def test_load_test_bank(self):
        game = Game()
        self.assertIsNotNone(game.testBank)
        self.assertIn('math', game.testBank['subjects'])

    @patch('Game.open', unittest.mock.mock_open(read_data='{"subjects": {"math": {"level1": [{"questionID": "1","question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "correctAnswer": "4"}]}}}'), create=True)
    def test_selectCategory_valid(self):
        game = Game()
        game.selectCategory('math')
        self.assertEqual(game.currentCategory, 'math')
        self.assertEqual(len(game.currentQuestions), 1)

    def test_startGame(self):
        with patch.object(Game, 'load_test_bank', return_value={}):
            game = Game()
            game.startGame('natetyu')
            self.assertEqual(game.player.playerId, 'natetyu')
            self.assertEqual(game.gameState, 'InProgress')

    @patch('Game.open', unittest.mock.mock_open(), create=True)
    def test_saveGame(self):
        game = Game()
        game.startGame('natetyu')
        game.currentCategory = 'math'
        game.saveGame()

    def test_nextLevel(self):
        with patch.object(Game, 'load_test_bank', return_value={}):
            game = Game()
            game.startGame('natetyu')
            game.currentLevel = 1
            game.nextLevel()
            self.assertEqual(game.currentLevel, 2)


if __name__ == '__main__':
    unittest.main()