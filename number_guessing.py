import random
from unicodedata import numeric

random_num = random.randint(1,50)
attempts = []
guess = int(input("Pick a number between 1 and 50\n"))



def guess_check(guess):
    while True:
        try:
            if guess > 50:
                guess = int(input('You are out of limits. Pick a number between 1 and 50\n'))
            else:
                break   
        except ValueError as err:
            print("Oh no!, that is not a valid value. Please type a numeric input")
            print("({})".format(err))
    return guess


while True:

    checked_guess = guess_check(guess)
    
    if checked_guess > random_num:
        attempts.append(checked_guess)
        print('Go Lower!')
        guess = int(input("Pick again\n"))
    elif checked_guess < random_num:
        attempts.append(checked_guess)
        print('Go Higher!')
        guess = int(input("Pick again\n"))
    elif checked_guess == random_num:
        attempts.append(checked_guess)
        print(f'Congratulations you guessed the right number on your {len(attempts)}th try!')
        print(attempts)
        break