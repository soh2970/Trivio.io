import unittest
from question2 import Question
from Player import Player
from unittest.mock import patch, MagicMock
from game import Game
from Boss import Boss
from Player import Player


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_load_test_bank(self):
        # Test that load_test_bank loads the test bank dictionary
        test_bank = self.game.load_test_bank()
        self.assertIsInstance(test_bank, dict)

    def test_select_category(self):
        # Test selectCategory method with valid category
        self.game.selectCategory('math')
        self.assertEqual(self.game.currentCategory, 'math')
        # Test selectCategory method with invalid category
        with self.assertRaises(ValueError):
            self.game.selectCategory('invalid_category')

    def test_start_game(self):
        # Test startGame method
        self.game.startGame('player_id')
        self.assertEqual(self.game.player.playerId, 'player_id')
        self.assertEqual(self.game.gameState, 'InProgress')

    def test_present_question(self):
        # Mocking random.choice to return a fixed question for testing
        with patch('random.choice') as mock_choice:
            mock_question_data = {
                'questionID': 1,
                'question': 'What is 2 + 2?',
                'options': [3, 4, 5, 6],
                'correctAnswer': 4
            }
            mock_choice.return_value = mock_question_data
            question = self.game.presentQuestion()
            self.assertIsInstance(question, Question)
            self.assertEqual(question.questionID, 1)
            self.assertEqual(question.question, 'What is 2 + 2?')

    def test_answer_question_correct(self):
        # Mocking player and question for testing
        self.game.player = Player('player_id', 100, 0, 1)
        question = Question(1, 'What is 2 + 2?', [3, 4, 5, 6], 4)
        self.game.answerQuestion(question, 4)
        self.assertEqual(self.game.player.playerScore, 1)
    
    def test_answer_question_incorrect(self):
        # Mocking player and question for testing
        self.game.player = Player('player_id', 100, 0, 1)
        question = Question(1, 'What is 2 + 2?', [3, 4, 5, 6], 4)
        self.game.answerQuestion(question, 3)
        self.assertEqual(self.game.player.playerHP, 96)

    def test_calculate_score(self):
        # Mocking player and question for testing
        self.game.player = Player('player_id', 100, 0, 1)
        question1 = Question(1, 'Question 1', [], 0)
        question2 = Question(2, 'Question 2', [], 0)
        self.game.player.questionsAnsweredCorrectly = [question1, question2]
        # Assuming each question has a weight of 1
        self.assertEqual(self.game.calculateScore(), 2)

    def test_next_level(self):
        # Mocking player for testing
        self.game.player = Player('player_id', 100, 0, 1)
        self.game.currentLevel = 1
        self.game.nextLevel()
        self.assertEqual(self.game.currentLevel, 2)
        # Testing reaching maximum level
        self.game.currentLevel = 3
        self.game.nextLevel()
        self.assertEqual(self.game.gameState, 'BossFight')

    def test_boss_fight(self):
        # Mocking player and boss for testing
        self.game.player = Player('player_id', 100, 0, 1)
        self.game.boss = Boss()
        self.game.boss.isBossDefeated = MagicMock(return_value=True)
        self.game.bossFight()
        self.assertEqual(self.game.gameState, 'Completed')

    def test_end_game(self):
        self.game.endGame()
        self.assertEqual(self.game.gameState, 'Completed')

    def test_save_game(self):
        # Mocking player and file operations for testing
        self.game.player = Player('player_id', 100, 0, 1)
        with patch('builtins.open', MagicMock()) as mock_open:
            self.game.saveGame()
            mock_open.assert_called_once()

    def test_load_game(self):
        # Mocking player and file operations for testing
        self.game.player = Player('player_id', 100, 0, 1)
        with patch('builtins.open', MagicMock()) as mock_open:
            self.game.loadGame()
            mock_open.assert_called_once()

    def test_exit_to_main_menu(self):
        # Mocking MainMenu for testing
        with patch('MainMenu.MainMenu') as mock_main_menu:
            self.game.exitToMainMenu()
            mock_main_menu.assert_called_once()


if __name__ == '__main__':
    unittest.main()