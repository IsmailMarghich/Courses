import sys
from random import randint
answer = randint(1, 10)
def run_guess(guess, answer): #the guessing part of the game is put into a function for testing
    if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                return True
    else:
        print('hey bozo, I said 1~10')
        return False
if __name__ == '__main__': #the game only runs when this is the main file
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue
