def swap(lyst,i,j):
    index = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = index

def selectionsort(lyst):
    i = 0
    while i < len(lyst) - 1:
        minindex = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst [minindex]:
                minindex = j
            j += 1
        if minindex != i:
            swap(lyst,minindex,i)
        i += 1

lm=[1,2,3,5,2,4]
selectionsort(lm)
        
            
        
