a = input('please input a word')
b = input('please input a letter')
i = 0
for letter in a :
    if letter == b:
        i += 1
if i == 0:
    print('find no',b)
else:
    print('find',i,b)

'''for a in range (1,10):
    print(a)'''
