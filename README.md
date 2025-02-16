# Trivio Game

## About our software
Trivio is a educational trivia game designed for school aged children ages 10-14. It includes 3 different subject categories - Math, Social Science, and Science, and the game contains 3 levels - easy (level 1), medium (level 2), and hard(level 3). The game tests student's level of knowledge in a fun and interactive way, where they compete to beat the 'boss' by answering questions correctly. 

Trivio was designed with python, using the pygame libarary. File formats handling data storage used the JSON format. It was developed using Visual Studio Code and Pycharm as development environments. 

## Required Libraries and Tools
Python v(3.11.3)<br>
pygame v(2.5.2)<br>
cx-Freeze v(6.15)<br>
<br>

Main Development Environment - Visual Studio Code v(1.83.2)<br>
Pycharm v(2023.3)

## Code Set Up and Running
Download and install all required libraries - python3, pygame, and the main development environment Visual Studio Code<br>

<a href="https://code.visualstudio.com/download">Link to download Visual studio Code</a>. To set up visual studio code, install Python in Extensions and open the file directory with the code. From there, the code files can be viewed. 

To download python3, head to the <a href="https://www.python.org/downloads/">python website</a> and download the 3.11.3 version. Once downloaded, open terminal and type ```python3 --version``` or ```python --version``` to check if the correct version was installed. 

To download pygame, in terminal type ```python3 -m pip install pygame```, or ```python -m pip install pygame```. If this doesn't work for you, go into the terminal and cd into the root of the project folder. Then type ```pip installl pygame```, or ```pip3 install pygame```.

Additionally, download the Trivio Zip file. It should automatically unzip once downloaded, however if not, right click and unzip to access the folder. 

Here are 2 different methods to running the code, in case of zip file issues:

### Step by Step compilation from development environment
Ensure that Visual Studio Code is set up with Python and includes Pygame. Otherwise, Visual Studio Code should automatically prompt for download of any missing libraries/extensions upon running.

1. In Visual Studio Code, select File -> Open Folder
2. Open the Trivio game main folder
3. In the Root folder, without opening any other folders, click the file <b>main.py</b>, which is the main game script
4. Run the main.py file to start the game


### Step by Step executuable compilation from source code 
1. Download and install cx_Freeze<br>

To download cx_Freeze, cd into the root of the Trivio folder. In terminal type ```pip install cx-Freeze```, or       ```pip3 install cx-Freeze``` and to check that the correct version is downloaded, in terminal type ```cxfreeze --version```

2. Open terminal and ```cd``` to the Trivio game root folder if not already there
3. Ensure that the <b>setup.py</b> file is in the root folder. Type the command ```python setup.py build``` to compile into the "main" file
4. After the build is completed, change directories from current to build, to exe.SOME_TEXT
For example, 
```cd build``` to get the exe file name. You may need to ```ls``` to get the exact name
```cd exe.SOME_TEXT``` to go into the executable folder
Then you need to move the images folder into the lib folder, for example:<br>
```mv images lib``` - MacOS and Linux<br>
```move images lib``` - Windows<br>

Then, you can run the executable main in terminal:<br>
```./main``` - MacOS and Linux<br>
```main``` - Windows


## User Guide
### Player
1. After running the game, you will be brought to the main welcome screen, and the background music will begin to play
2. Click Start to begin the game, X to quit the game, or select Options to change the volume of the background music
3. After clicking Start, you will be brought to the Login page, where you can either login as an existing user by entering the correct username and password combination that is stored in the playerBank json file, or create a new account by entering a desired username and password. If you try to create an account with a username already in the system, the program will provide an error and you will need to change the username before trying again
4. Instructors and Debuggers are also able to access the debugger and instructor password screens from this page as well, with the buttons for these screens at the top of the screen. You are also able to press X to exit the game as well
5. After logging in or creating an account, you will be brought to the new or saved game screen. If you are a new account, clicking the saved game button will display an error. If you have an exisiting saved game as a previous user, you can click this button and view your saved stats, as well as resume it from where you left off. Clicking the Scores button on the top left of the screen to view the highscore leaderboard for the game, and clicking X to quit the game.
6. Clicking new game for all users will bring you to the mode selection screen, where you can choose from the different game categories of Social Science, Science, or Math and begin playing. Players will also have the option to view the game tutorial screen through the Tuturial button, or begin the game with the desired category. They can also click the Back button to go back to the new or saved game screen
7. When you select a mode, you will be taken to the main game screen where the level you are on is displayed at the very top middle. Below this is the question being asked that must be answered. Your player character and the boss you are competing against have their icons displayed below, along with their current HP, both of which will update as the game continues. There are 4 big buttons displaying the answer options, with 3 incorrect answers and 1 correct one that must be selected. Once you have made your choice, click the associated button with the answer you wish to select, and the game will reveal a correct or incorrect answer screen which will show how much HP you or the boss have lost. Click continue to continue playing the game, which will turn to level 2 once the boss 80 HP, and level 3 once the boss hits 50 hp. If you ever run out of HP, you automatically lose the game, however once the Boss hits 0 HP, you win. To save progress at any point of the game, the user will need to press save game, and to adjust the volume at any point, they will need to press the options button. 
8. Upon winning or losing the game, a win game or lose game screen will be displayed with the users score, category, level, remaining boss HP, questions right and questions wrong. The user will then click next to view the highscore table, which will display the top 10 players high scores. They can then press mainn menu to be brought back to the new game or saved game screen. 

### Debugger and Instructor
1. After pressing Start Game, the Debugger and Instructor can access their associated login screens by clicking the debugger or instructor buttons at the top of the login page. 
2. Debugger enters the debug password and clicks okay to be brought to the debug menu where they are able to select a category and a mode and click next to view the question bank for that specific category at that specific level. If they click back they will be brought back to the debugger mode page where they can view other question banks, or home where they will be brought back to the login screen
3. Instructor enters the instructor password to be brought to the instructor mode page where they are able to enter a student's username an then view the last played timestamp, their current saved game level, subject, score, playerHP, bosssHP, number of questions correct, number of questions incorrect, and the players all time high score. 


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

Username - <i>sophiayuan</i>
Password - <b>123</b>

Username - <i>stephoh</i>
Password - <b>oh</b>

Username - <i>michaelkim</i>
Password - <b>0987</b>

Username - <i>harjapgrewal</i>
Password - <b>harjapgrewal</b>

## Additional Notes
The zip file executable ./main is not correctly running on one of our group members MacOS laptops. May need to use the development environment method to run the main.py class.


