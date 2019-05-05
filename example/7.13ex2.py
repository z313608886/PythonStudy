def find(word, start,letter):
    index = start
    while index < len(word):
        if word[index] == letter:
            print(word[0])
            return index
        index = index + 1
    return -1

a = find('sadasdhd',1,'h')
print(a)
