prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    a = letter + suffix
    if a == 'Oack':
        a = 'Ouack'
    elif a == 'Qack':
        a = 'Quack'
    print(a)

a = prefixes[1:3]
a = prefixes[2:5]
print(a)

a = 'ha'
b = 'jd'
print(a+b)
