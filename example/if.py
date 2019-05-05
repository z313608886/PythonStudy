number = 23
guess = int(input('Enter an integer:'))

if guess == number:
    print('congratulations,you guessed it.')
    print("(but you do not win any prizes！）")
elif guess < number:
    print('no,it\'s a little larger than that')
else:
    print('NO  it\'s a little lower than that')
print('done')
