def swap(lyst,i,j):
    index = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = index

def quicksort(lyst):
	quicksorthelper(lyst,0,len(lyst)-1)

def quicksorthelper(lyst,left,right):
	if left<right:
		pivotloction = partition (lyst)