'''
Highscore
Pawelski
4/19/2023
Python II

Instructions:
First, let's read the code to understand what each part
of the program does. What does the generate_question()
function do? What does the check_new_highscore() function
do? What does the update_highscore() function do? What
does the main part of the program do? Based on this code,
how do functions help manage the complexity of the main?

Run the program and play the game. Run the program again
and play until you beat the highscore. OH NO! There is an
error. On what line? What is wrong with the program. How
do we fix the error? Based on this program, why would we
ever want to use create mode ("x")? Also, why is it a good
idea to check if a file exists before opening the file and
reading from it?
'''

import random, os


def generate_question():
    '''
    Generates a single questions and reports whether
    the user got the question correct.
    '''
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    guess = int(input(str(number1) + " + " + str(number2) + " = "))
    return guess == number1 + number2


def update_highscore(file_name, score):
    '''
    Updates the highscore file.
    '''
    highscore_file = open(file_name, "x")
    print("Congratulations, you got the highscore!")
    name = input("Enter your name >> ")
    highscore_file.write(name + "\n" + str(score))
    highscore_file.close()


def check_new_highscore(score):
    '''
    First checks whether "highscore.txt" has been created
    yet. If not, it automatically creates the document
    and logs the score as the highscore. If the document
    exists, the program reads the highscore and checks if
    the user's score beat the highscore.
    '''
    file_name = "highscore.txt"
    if os.path.exists(file_name):
        highscore_file = open(file_name)
        highscore = highscore_file.readlines()
        highscore_file.close()
        if score > int(highscore[1].strip()):
            update_highscore(file_name, score)
        else:
            print("Try again to get the highscore!")
            print(highscore[0].strip() + " got a highscore of "
                  + highscore[1])
    else:
        update_highscore(file_name, score)


print("How many questions can you get correct?")
questions_correct = 0
while generate_question():
    questions_correct += 1
check_new_highscore(questions_correct)
