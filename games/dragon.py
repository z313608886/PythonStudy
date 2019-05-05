import random
import time

def displayintro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave,the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry,and will eat you on first sight')
    print()

def choosecave():
    cave = ''
    while cave != '1' and cave != '2':
        print('which cave will you go into?(1 or 2)')
        cave = input()
    return cave

def checkcave(choosecave):
    print('you approach the cave……')
    time.sleep(2)
    print('it\'s dark and spooky……')
    time.sleep(2)
    print('a dragon jumps out in front of you! he opens his jaws and……')
    print()
    time.sleep(2)
    friendlycave = random.randint(1,2)
    if int(choosecave) == friendlycave:
        print('give you his treasure')
    else:
        print('Gobbles you down in one bite')

playagain = 'Yes'
while playagain == 'Yes' or playagain == 'Y':
    displayintro()
    cavenumber = choosecave()
    checkcave(cavenumber)
    print('if you want to play again?')
    playagain = input()





