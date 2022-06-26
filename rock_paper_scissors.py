import random
import os


os.system('cls' if os.name=='nt' else 'clear')
choices = ["R","P","S"]

def choose():
    print ("Rock, Paper, Scissors - Shoot!")
    pick = input("Choose your weapon [R]ock], [P]aper, [S]cissors or [E]xit: ")
    if pick.upper()[0] not in choices and pick.upper()[0] != 'E':
        pick = input("Please choose one of these weapons [R]ock], [P]aper, [S]cissors or [E]xit: ")
    return pick

while True:

    pick = choose()

    if pick.upper()[0] == random.choice(choices):
        print("It's a TIE!")
        continue
    elif pick.upper()[0] == 'R' and random.choice(choices) == 'P':
        print("You chose: 'Rock'\nI chose:'Paper'\nI won!")
        continue
    elif pick.upper()[0] == 'R' and random.choice(choices) == 'S':
        print("You chose: 'Rock'\nI chose:'Scissors'\nYou win!")
        continue
    elif pick.upper()[0] == 'P' and random.choice(choices) == 'R':
        print("You chose: 'Paper'\nI chose:'Rock'\nYou win!")
        continue
    elif pick.upper()[0] == 'P' and random.choice(choices) == 'S':
        print("You chose: 'Paper'\nI chose:'Scissors'\nI won!")
        continue
    elif pick.upper()[0] == 'S' and random.choice(choices) == 'R':
        print("You chose: 'Scissors'\nI chose:'Rock'\nI won!")
        continue
    elif pick.upper()[0] == 'S' and random.choice(choices) == 'P':
        print("You chose: 'Scissors'\nI chose:'Scissors'\nYou win!")
        continue
    elif pick.upper()[0] == "E":
        break

