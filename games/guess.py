import random
b = random.randint(1, 20)  #生成随机数
print('hello! What is your name?')
name = input()
print('Well,', name, ', I am thinking of a number between 1 and 20.')
print('take a guess.')
c = True
d = 0
while c:
    a = input()
    d = d+1
    if a == 'end':
        print('Game over')
        break
        # c=False 改变c的取值也可以跳出while循环
    else:
        a = int(a)
        if a > b:
            print('Your guess is too high. \n Guess again')
        elif a < b:
            print('Your guess is too low. \n Guess again')
        else:
            print('Good job', name, 'You guessed my number in', d, 'guesses!')

