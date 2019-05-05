number = 23
running = True
while running:
    guess = int(input('enter an integer:'))
    if guess == number:
        print('you got it')
        running = False
    elif guess < number:
        print('higher than that')
    else:
        print("lower than that")

print('loop is over')
print('Done')
