import random
from unicodedata import numeric

random_num = random.randint(1,100)
number = int(input("Guess the Number from 1 to 50!!!! "))

def check_num(number):
    while True:
        if number > 50:
            number = int(input('You are out of limits. Guess again '))
        else:
            break
    return number
 
while True:

    number_checked = check_num(number)
    if number_checked > random_num:
        number = int(input('You are high. Go Lower! '))
    elif number_checked < random_num:
        number = int(input('You are low. Go Higher! '))
    elif number == random_num:
        print('Congratulations you guessed right!')
        break
    
