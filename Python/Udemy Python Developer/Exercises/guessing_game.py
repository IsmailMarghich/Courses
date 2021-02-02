#create a guessing game but using sys.argv as an input for your program
#run this file and dont mind the error, and then run the file from your terminal and use 2 arguments as your start and stop
#for your guessing game, i.e '1 10' gives you a game where u have to guess a number between 1 and 10
from random import randint
import sys
answer = randint(int(sys.argv[1]), int(sys.argv[2])) # generate number between the terminal inputs

while True:
    try: # constant loop that tries converting input into integers
        guess = int(
            input(f'guess a number between {int(sys.argv[1])} and {int(sys.argv[2])}: '))
        if int(sys.argv[1]) < guess < int(sys.argv[2]):  # checks wether input is within the terminal input
            if guess == answer:
                print('guessed correctly') #if the guess is same as answer print you guessed it correctly and cotninue
                continue
            else:
                print('you guessed wrongly') #if the guess is wrong then print its wrong and continue
                continue
        else:
            print('enter a number between 1 and 10 please')
    except ValueError: #if the input cant be converted to integers then print only enter numbers and go back to the top
        print('please enter only numbers')
