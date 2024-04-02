
import sys
import os
import unittest
import pygame


from Player import Player
from Level import Level
from Boss import Boss
from HighScorer import HighScore
from UserAccount import UserAccount



class TestPlayer(unittest.TestCase):
    """
    Unit tests for the Player class.

    Methods:
        setUp():
            Prepares the environment before each test method execution.
        tearDown():
            Cleans up the environment after each test method execution.
        test_loseHp():
            Tests the losePlayerHP method of the Player class.
        test_defeat():
            Tests the isPlayerDefeated method of the Player class.
        test_incrementScore():
            Tests the incrementScore method of the Player class.
        test_moveNextLevel():
            Tests the moveToNextLevel method of the Player class.
    """

    def setUp(self):
        print("\nRunning setUp method...")
        self.player = Player('harjap', 100, 100, 1)

    def tearDown(self):
        print("Running tearDown method...")


    def test_loseHp(self):
        self.player.losePlayerHP(1)
        self.assertEqual(self.player.playerHP, 96)
        self.player.losePlayerHP(2)
        self.assertEqual(self.player.playerHP, 90)
        self.player.losePlayerHP(3)
        self.assertEqual(self.player.playerHP, 80)

    def test_defeat(self):
        self.assertFalse(self.player.isPlayerDefeated())
        self.player.playerHP = 0
        self.assertTrue(self.player.isPlayerDefeated())
    
    def test_incrementScore(self):
        self.player.incrementScore()
        self.assertEqual(self.player.playerScore, 104)
        self.player.currentLevel = 2
        self.player.incrementScore()
        self.assertEqual(self.player.playerScore, 110)
        self.player.currentLevel = 3
        self.player.incrementScore()
        self.assertEqual(self.player.playerScore, 120)
    
    def test_moveNextLevel(self):
        self.player.moveToNextLevel(2)
        self.assertEqual(self.player.currentLevel, 2)
        with self.assertRaises(Exception):
            self.player.moveToNextLevel(5)
            




class TestLevel(unittest.TestCase):
    """
    Unit tests for the Level class.

    Methods:
        setUp():
            Prepares the environment before each test method execution.
        tearDown():
            Cleans up the environment after each test method execution.
        test_moveToNextLevel():
            Tests the moveToNextLevel method of the Level class.
    """
    # Not testing completeLevel

    def setUp(self):
        print("\nRunning setUp method...")
        self.level = Level(1, 'math')

    def tearDown(self):
        print("Running tearDown method...")


    def test_moveToNextLevel(self):
      self.level.moveToNextLevel(2)
      self.assertEqual(self.level.levelNum, 2)
    

class TestBoss(unittest.TestCase):
    """
    Unit tests for the Boss class.

    Methods:
        setUp():
            Prepares the environment before each test method execution.
        tearDown():
            Cleans up the environment after each test method execution.
        test_loseBossHp():
            Tests the loseBossHp method of the Boss class.
        test_bossDefeated():
            Tests the isBossDefeated method of the Boss class.
    """
    def setUp(self):
        print("\nRunning setUp method...")
        self.boss = Boss()

    def tearDown(self):
        print("Running tearDown method...")


    def test_loseBossHp(self):
        self.boss.loseBossHP(1)
        self.assertTrue(self.boss.bossHp,96)
        self.boss.loseBossHP(2)
        self.assertTrue(self.boss.bossHp,90)
        self.boss.loseBossHP(3)
        self.assertTrue(self.boss.bossHp,80)
        
        with self.assertRaises(Exception):
            self.boss.loseBossHP(5)

    
    def test_bossDefeated(self):
        self.assertFalse(self.boss.isBossDefeated())
        self.boss.bossHp = 0
        self.assertTrue(self.boss.isBossDefeated())


class TestHighScore(unittest.TestCase):
    """
    Unit tests for the HighScore class.

    Methods:
        setUp():
            Prepares the environment before each test method execution.
        tearDown():
            Cleans up the environment after each test method execution.
        test_checkForScore():
            Tests the checkForScore method of the HighScore class.
        test_playerInfo():
            Tests the getPlayerGameInfo method of the HighScore class.
    """
    def setUp(self):
        print("\nRunning setUp method...")
        self.highscore = HighScore()

    def tearDown(self):
        print("Running tearDown method...")


    def test_checkForScore(self):
        self.assertTrue(self.highscore.checkForScore(''))
        self.assertFalse(self.highscore.checkForScore('NeverGonnaGiveYouUp'))        
    
    def test_playerInfo(self):
        self.assertIs(type(self.highscore.getPlayerGameInfo('')), dict)


class TestUserAccount(unittest.TestCase):
    """
    Unit tests for the UserAccount class.

    Methods:
        setUp():
            Prepares the environment before each test method execution.
        tearDown():
            Cleans up the environment after each test method execution.
        test_login():
            Tests the validateLogin method of the UserAccount class.
        test_createAccount():
            Tests the createAccount method of the UserAccount class.
    """
    def setUp(self):
        print("\nRunning setUp method...")
        self.account = UserAccount('', '')

    def tearDown(self):
        print("Running tearDown method...")


    def test_login(self):
        self.assertTrue(self.account.validateLogin())
    
    def test_createAccount(self):
        with self.assertRaises(Exception):
            self.account.createAccount()



           
if __name__ == '__main__':
    unittest.main()
    


