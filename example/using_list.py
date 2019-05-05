# this is my shopping list
shoplist = ['apple','mango','carrot','banana']

print('i have {0} items to buy '.format(len(shoplist)))

print('these items are:',end='')
for item in shoplist:
    print(item, end=' ')

print('\n i also need to buy rice.')
shoplist.append('rice')
print('My shopping list is now',shoplist)

print('sort list')
shoplist.sort()
print('sorted list is',shoplist)

del shoplist[0]
print(shoplist)
