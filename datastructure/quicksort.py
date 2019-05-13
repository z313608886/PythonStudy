def swap(lyst,i,j):
    index = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = index

def quicksort(lyst):
	quicksorthelper(lyst,0,len(lyst)-1)

def quicksorthelper(lyst,left,right):   #递归函数
	if left<right:
		pivotloction = partition(lyst,left,right)
		quicksorthelper(lyst,left,pivotloction-1)
		quicksorthelper(lyst,pivotloction+1,right)

def partition(lyst,left,right):
	middle = (left +right)//2
	pivot = lyst[middle]
	lyst[middle] = lyst[right]
	lyst[right] = pivot
	boundary = left
	for index in range(left,right):
		if lyst[index]<pivot:
			swap(lyst,index,boundary)
			boundary += 1
	swap(lyst,right,boundary)
	return boundary

import random
def main(size=5,sort=quicksort):
	lyst=[]
	for count in range(size):
		lyst.append(random.randint(1,size+1))
		print(lyst)
		sort(lyst)
		print(lyst)
	#print((1+2)//2)  结果为1

if __name__=='__main__':
	main()
