import random
from unicodedata import numeric

random_num = random.randint(1,50)
number = int(input("Guess the Number from 1 to 50!!!! \n"))
list_of_guess = []

def check_num(number):
    while True:
        if number > 50:
            number = int(input('You are out of limits. Guess again \n'))
        else:
            break
    return number


 
while True:

    number_checked = check_num(number)
    if number_checked > random_num:
        list_of_guess.append(number_checked)
        number = int(input('You are high. Go Lower! \n '))
    elif number_checked < random_num:
        list_of_guess.append(number_checked)
        number = int(input('You are low. Go Higher! \n '))
    elif number == random_num:
        list_of_guess.append(number_checked)
        print(f'Congratulations you guessed the right number on your {len(list_of_guess)}th try!')
        print(list_of_guess)
        break
    
