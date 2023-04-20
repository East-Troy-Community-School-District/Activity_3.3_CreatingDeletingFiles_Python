'''
Class Rosters
Pawelski
4/19/2023
Python II

Instructions:
Run the program and enter the rosters for at least two teachers.
How many files were created? What was used for the name of the file?
Why did this program check if the file existed before creating a
new one?
'''

import os


def fill_roster(file_name):
    '''
    Asks for all the names on the roster and writes them to a file.
    '''
    file = open(file_name + ".txt", "x")
    name = input("Enter the name of a student (zzzzz to quite) >> ")
    while name != "zzzzz":
        file.write(name + "\n")
        name = input("Enter the name of a student (zzzzz to quite) >> ")
    file.close()


teacher_name = input("Enter the name of the teacher for the roster (zzzzz to quite) >> ")
while teacher_name != "zzzzz":
    if os.path.exists(teacher_name + ".txt"):
        print("Invalid! A teacher may only have one roster.")
    else:
        fill_roster(teacher_name)
    print()
    teacher_name = input("Enter the name of the teacher for the roster (zzzzz to quite) >> ")