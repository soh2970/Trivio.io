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
1. 

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



