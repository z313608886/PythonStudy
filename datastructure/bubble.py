def swap(lyst,i,j):
    index = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = index

def bubblesort(lyst):
    n = len(lyst)
    while n > 1:
        i = 0
        while i+1 < n:
            if lyst[i] > lyst[i+1]:
                swap(lyst,i,i+1)
            i += 1
        n -= 1

def bubblesortwihtweak(lyst):
    n = len(lyst)
    while n > 1:
        i = 0
        swapped = False
        while i+1 < n:
            if lyst[i] > lyst[i+1]:
                swap(lyst,i,i+1)
                swapped = True
            i += 1
        if not swapped: return
        n -= 1

lm=[3,7,1,2,8,4]
bubblesort(lm)
bubblesortwihtweak(lm)
