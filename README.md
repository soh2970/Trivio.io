# Trivio Game

Your README file should include the following:

A short description of your software and what it does.
A list of the required libraries and third party tools required to run or build your software (include version numbers).
A detailed step by step guide for building your software (compiling it from source code). This should include details on how to obtain and install any third party libraries.
A detailed step by step guide on how to run your already built (compiled) software.
A user guide, that explains how to use your software.
If your software uses accounts, a password, or pin you must include any account username/password, pin, etc. required to use your software.
You must also include details on how to access your teacher mode and steps to build/install it if it is a separate program.
Anything else that would be helpful for the TA marking your project to know.
This README file should be in the root directory of your repository and in your submitted zip archive.

## About our software
Trivio is a educational trivia game designed for school aged children ages 10-14. It includes 3 different subject categories - Math, Social Science, and Science, and the game contains 3 levels - easy (level 1), medium (level 2), and hard(level 3). The game tests student's level of knowledge in a fun and interactive way, where they compete to beat the 'boss' by answering questions correctly. 

Trivio was designed with python, using the pygame libarary. File formats handling data storage used the JSON format. It was developed using Visual Studio Code and Pycharm as development environments. 

## Required Libraries and Tools
Python v(3.9.13)<br>
pygame v(2.5.2)<br>
<br>

Visual Studio Code v(1.83.2)<br>
Pycharm v(2023.3)

## Step by Step guide to compiling from source code
1. Make sure cx_Freeze is installed, this is to compile source code into an executable file.
2. Install cx_Freeze by typing "pip install cx_Freeze"
3. Open terminal and in the project directory, run the command "python setup.py build"
4. After the build is complete, change directories from current-->build-->exe.sometext
5. Move the images folder into the lib folder


## Step by Step guide to running compiled software
1. From terminal, in the exe.sometext directory, type "./main"
2. Trivio will now run


## User Guide
### Player
1. After running the game, you will be brought to the main welcome screen, and the background music will begin to play
2. Click Start to begin the game, X to quit the game, or select Options to change the volume of the background music
3. After clicking Start, you will be brought to the Login page, where you can either login as an existing user by entering the correct username and password combination that is stored in the playerBank json file, or create a new account by entering a desired username and password. If you try to create an account with a username already in the system, the program will provide an error and you will need to change the username before trying again
4. Instructors and Debuggers are also able to access the debugger and instructor password screens from this page as well, with the buttons for these screens at the top of the screen. You are also able to press X to exit the game as well
5. After logging in or creating an account, you will be brought to the new or saved game screen. If you are a new account, clicking the saved game button will display an error. If you have an exisiting saved game as a previous user, you can click this button and view your saved stats, as well as resume it from where you left off. Clicking the Scores button on the top left of the screen to view the highscore leaderboard for the game, and clicking X to quit the game.
6. Clicking new game for all users will bring you to the mode selection screen, where you can choose from the different game categories of Social Science, Science, or Math and begin playing. Players will also have the option to view the game tutorial screen through the Tuturial button, or begin the game with the desired category. They can also click the Back button to go back to the new or saved game screen
7. When you select a mode, you will be taken to the main game screen where the level you are on is displayed at the very top middle. Below this is the question being asked that must be answered. Your player character and the boss you are competing against have their icons displayed below, along with their current HP, both of which will update as the game continues. There are 4 big buttons displaying the answer options, with 3 incorrect answers and 1 correct one that must be selected. Once you have made your choice, click the associated button with the answer you wish to select, and the game will reveal a correct or incorrect answer screen which will show how much HP you or the boss have lost. Click continue to continue playing the game, which will turn to level 2 once the boss 80 HP, and level 3 once the boss hits 50 hp. If you ever run out of HP, you automatically lose the game, however once the Boss hits 0 HP, you win.
8. Upon winning or losing the game. 

### Debugger and Instructor


## Passwords and User Accounts
### Teacher (Instructor Mode)
1. The Log-in screen includes 3 buttons on the top left corner, the exit game button, Instructor Mode, and Debugger Mode
2. Click Instructor Mode to be taken the the instructor log-in screen
3. Enter the password <b>instruct</b> in all lower case without the brackets around and click ok
4. You should be taken to the instructor dashborad screen
5. Type in a username in the search bar to find a student 

### Debugger Mode Password
The debugger mode password is: <b>debug</b>

### User Accounts
Username - <i>nateyu</i>
Password - <b>hello</b>

Username - <i>hihi</i>
Password - <b>123</b>

Username - <i>stephoh</i>
Password - <b>123</b>

## Additional Notes



