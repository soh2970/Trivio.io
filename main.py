import sys
import os


# Assuming main.py is in the root directory of personalRepo2212
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Set the working directory to the directory of main.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))
"""
#options screen logic 
        if (current_screen.type == "OptionsScreen"):
            current_screen.draw()
            current_screen.handle_events()
            if (current_screen.back == True):
                current_screen = GameScreen('math', current_player, boss, level.getNextQuestion(), level.levelNum, score)
    needs to be in every game screen
"""


import pygame
from src.UIs.screen import ScreenBase
from src.UIs.AudioManager import AudioManager
from src.UIs.GameScreen2 import GameScreen
from src.question2 import Question
from src.Level import Level
from src.Player import Player
from src.Boss import Boss
from src.game import Game
from src.MainMenu import MainMenu
from src.UIs.NewSavedGameScreen import NewSavedGameScreen
from src.UIs.GameModeSelectScreen import GameModeSelectScreen
from src.UIs.WelcomeScreen import WelcomeScreen
from src.UIs.LoginScreen import LoginScreen
from src.UIs.CorrectAnswerScreen import CorrectAnswerScreen
from src.UIs.LoadGameScreen import LoadGameScreen
from src.UIs.DebuggerPasswordScreen import DebuggerPasswordScreen
from src.UIs.IncorrectAnswerScreen import IncorrectAnswerScreen
from src.UIs.DebuggerDashboardScreen import DebuggerDashboardPage
from src.UIs.DebuggerModeScreen import DebuggerModeScreen
from src.UIs.InstructorPasswordScreen import InstructorPasswordScreen
from src.UIs.H_InstructorDashboardScreen import InstructorDashboardScreen
from src.UIs.OptionsScreen import OptionsScreen
from src.UIs.WinLevelScreen import WinLevelScreen
from src.UIs.WinGameScreen import WinGameScreen
from src.UIs.HighscoreLeaderboardScreen import LeaderboardScreen
from src.UIs.TutorialScreen1 import GameTutorialScreenOne
from src.UIs.TutorialScreen2 import ScoringTutorialScreenTwo
from src.UIs.LoseGameScreen import LoseGameScreen


audio_manager = AudioManager()

def run_game():

    audio_manager.__init__()
    audio_manager.play_song()

    running = True
    screen = pygame.display.set_mode((844,600), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    current_player = None
    boss = Boss()
    score = 0
    questions_correct = 0
    questions_incorrect = 0


    current_screen = WelcomeScreen(audio_manager)
    level = Level(1, 'science')

    while running:
        #initial welcome screen
        if (current_screen.type == 'welcomeScreen'):
            current_screen.draw()
            current_screen.handle_events()
            if (current_screen.transitionToNextScreen): current_screen = LoginScreen()


        if current_screen.type == 'winLevel':
            current_screen.draw()
            current_screen.handle_events()
            level = level.levelNum + 1
            

        #login screen logic
        if current_screen.type == 'loginScreen':
            current_screen.draw()
            current_screen.handle_events()

            if current_screen.isValidUser:
                current_player = current_screen.Player
                current_screen = NewSavedGameScreen(current_player)
                print(current_player.playerId)

            elif current_screen.transitionToDebuggerPassword:
                print("transitioning to debugger password screen")
                current_screen = DebuggerPasswordScreen()

            elif current_screen.transitionToInstructorPassword:
                print("transitioning to instructor password screen")
                current_screen = InstructorPasswordScreen()

        #instructor screen logics
        if current_screen.type == 'instructorPassword':
            current_screen.draw()
            current_screen.handle_events()

            if current_screen.transitionToLogin:
                print("Transitioning to Login Screen")
                current_screen = LoginScreen()

            elif current_screen.transitionToDashboard:
                print("Transitioning to Instructor Dashboard...")
                current_screen = InstructorDashboardScreen()
                

        #logic for InstructorDashboard goes here
        if current_screen.type == 'instructorDashboard':
            current_screen.draw()
            current_screen.handle_events()

            if current_screen.transitionToLogin:
                print("Transitioning to Login screen...")
                current_screen = LoginScreen()

        #debugger screen logics
        if current_screen.type == 'debuggerPassword':
            current_screen.draw()
            current_screen.handle_events()

            if current_screen.transitionToDashboard:
                print("Transitioning to Debugger Dashboard...")
                current_screen = DebuggerDashboardPage( )

            elif current_screen.transitionToLogin:
                print("Transitioning to Login Screen")
                current_screen = LoginScreen()

        if current_screen.type == 'debuggerDashboard':
            current_screen.draw()
            current_screen.handle_events()

            if current_screen.transitionToModeScreen:
                print("Transitioning to Debugger Mode Screen...")
                current_screen = DebuggerModeScreen(current_screen.selectedCategory, current_screen.selectedLevel)

            elif current_screen.transitionToLogin:
                print("Transitioning to Login Screen")
                current_screen = LoginScreen()

    
        if current_screen.type == 'debuggerModeScreen':
            current_screen.draw()
            current_screen.handle_events()

            if current_screen.transitionToLogin:
                print("Transitioning to Login Screen...")
                current_screen = LoginScreen()

            elif current_screen.transitionToDashboard:
                print("Transitioning to Debugger Dashboard Screen...")
                current_screen = DebuggerDashboardPage()

        #main menu logic
        if (current_screen.type == "newSavedGameScreen"):
            current_screen.draw()
            current_screen.handle_events()
            if (current_screen.transitionToNewGame == True):
                print("transitioning to category select screen")
                current_screen = GameModeSelectScreen()
            elif (current_screen.transitionToLoadGame == True):
                print("user wants to load game")
                current_screen = LoadGameScreen(current_player)

            elif current_screen.transitionToLeaderboard == True: 
                print("user wants to leaderboard")
                current_screen = LeaderboardScreen()

        if current_screen.type == "highscoreLeaderboard":
            current_screen.draw()
            current_screen.handle_events()

            if current_screen.goToMain == True:
                current_screen = NewSavedGameScreen(current_player)
        
        #load game screen logic
        if (current_screen.type == "loadGameScreen"):
            current_screen.draw()
            current_screen.handle_events()
            #checks if user wants to go back to main menu
            if (current_screen.back == True):
                current_screen = NewSavedGameScreen(current_player)

            #logic for if a user wants to continue the saved game
            elif (current_screen.userContinue == True):
                #initialize player HP
                current_player.playerHP = int(current_screen.currentSave['playerHP'])
                #initialize boss HP
                boss.bossHp = int(current_screen.currentSave['bossHP'])
                #initialize level
                levelNum = int(current_screen.currentSave['levelAchieved'])
                category = current_screen.currentSave['subject']
                level = Level(levelNum, category)

                questions_correct = current_screen.questions_correct
                questions_incorrect = current_screen.questions_incorrect

                #initialize score
                score = int(current_screen.currentSave['score'])
                
                #switch to game screen with saved game data
                current_screen = GameScreen(category, current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)





        #game mode selection logic
        if (current_screen.type == 'gameModeSelect'):
            current_screen.draw()
            current_screen.handle_events()
            if (current_screen.choice == 'back'):
                print('back to main menu')
                current_screen = NewSavedGameScreen(current_player)
            elif (current_screen.choice == 'math'):
                print("math was chosen")
                level = Level(1, 'math')
                current_screen = GameScreen('math', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)
            elif (current_screen.choice == 'social_sciences'):
                print("social science was chosen")
                level = Level(1, 'social_sciences')
                current_screen = GameScreen('social_sciences', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)
            elif (current_screen.choice == 'science'):
                print("science was chosen")
                level = Level(1, 'science')
                current_screen = GameScreen('science', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)

            elif current_screen.choice == 'tutorial':
                print('to tutorial screen')
                current_screen = GameTutorialScreenOne()

        if current_screen.type == 'tutorialOne':
            current_screen.draw()
            current_screen.handle_events()

            if current_screen.toNextPage:
                current_screen = ScoringTutorialScreenTwo()
            elif current_screen.toGameMode:
                current_screen = GameModeSelectScreen()

        if current_screen.type == 'tutorialTwo':
            current_screen.draw()
            current_screen.handle_events()

            if current_screen.prevTut:
                current_screen = GameTutorialScreenOne()
            elif current_screen.toGameMode:
                current_screen = GameModeSelectScreen()



        # math gameplay
        if (current_screen.type == 'math'):
            current_screen.draw()
            current_screen.handle_events()

            if (current_screen.answered):
                # Increase global score
                score = current_screen.score
                # Correct answer screen displayed
                if (current_screen.answeredCorrectly == True):
                    questions_correct += 1
                    current_screen = CorrectAnswerScreen(level.levelNum)
                else:
                    questions_incorrect += 1
                    current_screen = IncorrectAnswerScreen(level.levelNum)
                    
                while (current_screen.nextQuestion == False):
                    current_screen.draw()
                    current_screen.handle_events()
                    pygame.display.flip()

                #increase level based on remaining boss HP
                if (boss.bossHp <= 0) or (current_player.playerHP <= 0):
                    #lose game screen /// win game screen
                    #high score leaderboard screen

                    current_screen = GameScreen('math', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)
                    current_screen.endGame()
                    if (boss.bossHp <= 0):
                        score = score * current_player.playerHP
                        current_screen = WinGameScreen(score)

                    elif (current_player.playerHP <= 0):
                        current_screen = LoseGameScreen('math', level.levelNum, boss.bossHp, questions_correct, questions_incorrect, score)
                
                elif (boss.bossHp <= 50 and boss.bossHp > 0):
                    #show level passed
                    if level.levelNum != 3:
                        level.moveToNextLevel(3)
                        current_screen = GameScreen('math', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)

                elif (boss.bossHp <= 80 and boss.bossHp > 50):
                    #show level passed
    
                    if level.levelNum != 2:
                        level.moveToNextLevel(2)
                        current_screen = GameScreen('math', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)

                if (current_screen.type != 'winGameScreen' and current_screen.type != 'loseGameScreen'):
                    current_screen = GameScreen('science', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)


        if current_screen.type == "options":
            current_screen.draw()
            current_screen.handle_events()



        #science gameplay
        if (current_screen.type == 'science'):
            current_screen.draw()
            current_screen.handle_events()

            if (current_screen.answered):
                # Increase global score
                score = current_screen.score
                if (current_screen.answeredCorrectly == True):
                    questions_correct += 1
                    current_screen = CorrectAnswerScreen(level.levelNum)
                else:
                    questions_incorrect += 1
                    current_screen = IncorrectAnswerScreen(level.levelNum)
                    


                while (current_screen.nextQuestion == False):
                    current_screen.draw()
                    current_screen.handle_events()
                    pygame.display.flip()


                if (boss.bossHp <= 0) or (current_player.playerHP <= 0):
                    current_screen = GameScreen('science', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)
                    current_screen.endGame()
                    if (boss.bossHp <= 0):
                        score = score * current_player.playerHP
                        current_screen = WinGameScreen(score)
                    elif (current_player.playerHP <= 0):
                        current_screen = LoseGameScreen('science', level.levelNum, boss.bossHp, questions_correct, questions_incorrect, score)

                elif (boss.bossHp <= 50 and boss.bossHp > 0):
                    if level.levelNum != 3:
                        level.moveToNextLevel(3)
                        current_screen = GameScreen('science', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)

                elif (boss.bossHp <= 80 and boss.bossHp > 50):
                    if level.levelNum != 2:
                        level.moveToNextLevel(2)
                        current_screen = GameScreen('science', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)

                if (current_screen.type != 'winGameScreen' and current_screen.type != 'loseGameScreen'):
                    current_screen = GameScreen('science', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)

                
    

        #social science gameplay
        if (current_screen.type == 'social_sciences'):
            current_screen.draw()
            current_screen.handle_events()

            if (current_screen.answered):
                # Increase global score
                score = current_screen.score
                # Correct answer screen displayed
                if (current_screen.answeredCorrectly == True):
                    questions_correct += 1
                    current_screen = CorrectAnswerScreen(level.levelNum)
                else:
                    questions_incorrect += 1
                    current_screen = IncorrectAnswerScreen(level.levelNum)
                    
                while (current_screen.nextQuestion == False):
                    current_screen.draw()
                    current_screen.handle_events()
                    pygame.display.flip()
                if (boss.bossHp <= 0) or (current_player.playerHP <= 0):
                    current_screen = GameScreen('social_sciences', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)
                    current_screen.endGame()
                    if (boss.bossHp <= 0):
                        score = score * current_player.playerHP
                        current_screen = WinGameScreen(score)

                    elif (current_player.playerHP <= 0):
                        current_screen = LoseGameScreen('social_sciences', level.levelNum, boss.bossHp, questions_correct, questions_incorrect, score)
                    
                elif (boss.bossHp <= 50 and boss.bossHp > 0):
                    if level.levelNum != 3:
                        level.moveToNextLevel(3)
                        current_screen = GameScreen('social_sciences', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)

                elif (boss.bossHp <= 80 and boss.bossHp > 50):
                    if level.levelNum != 2:
                        level.moveToNextLevel(2)
                        print('moving to next level')
                        current_screen = GameScreen('social_sciences', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)

                if (current_screen.type != 'winGameScreen' and current_screen.type != 'loseGameScreen'):
                    current_screen = GameScreen('social_sciences', current_player, boss, level.getNextQuestion(), level.levelNum, score, audio_manager, questions_correct, questions_incorrect)


        if (current_screen.type == 'winGameScreen'):
            current_screen.draw()
            current_screen.handle_events()

            #user clicks next to return to main menu
            if (current_screen.returnToMenu == True):
                score = 0
                boss = Boss()
                level = Level(1, 'science')
                current_player.playerHP = 100
                questions_correct = 0
                questions_incorrect = 0
                current_screen = NewSavedGameScreen(current_player)

        if (current_screen.type == 'loseGameScreen'):
            current_screen.draw()
            current_screen.handle_events()

            #user clicks next to return to the main menu
            if (current_screen.returnToMenu == True):
                score = 0
                boss = Boss()
                level = Level(1, 'science')
                current_player.playerHP = 100
                questions_correct = 0
                questions_incorrect = 0
                current_screen = NewSavedGameScreen(current_player)

        pygame.display.flip()
        
if __name__ == "__main__":
    run_game()