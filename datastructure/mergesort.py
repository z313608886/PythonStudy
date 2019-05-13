import random
import array

def mergesort(lyst):
	copybuffer = array.array('i',[0])
	for i in range(1,len(lyst)):
		copybuffer.append(0)
	mergesorthelper(lyst,copybuffer,0,len(lyst)-1)

def mergesorthelper(lyst,copybuffer,low,high):
	if low < high:
		middle = (low + high)//2
		mergesorthelper(lyst,copybuffer,low,middle)
		mergesorthelper(lyst,copybuffer,middle + 1,high)
		merge(lyst,copybuffer,low,middle,high)

def merge(lyst,copybuffer,low,middle,high):
	i1 = low
	i2 = middle + 1
	for i in range(low,high+1):
		if i1 > middle:
			copybuffer[i] = lyst[i2]
			i2 += 1
		elif i2 > high:
			copybuffer[i] = lyst[i1]
			i1 += 1
		elif lyst[i1] < lyst[i2]:
			copybuffer[i] = lyst[i1]
			i1 += 1
		else:
			copybuffer[i] = lyst[i2]
			i2 += 1
	for i in range(low,high+1):
		lyst[i] = copybuffer[i]

def main():
	lyst =[]
	for i in range(10):
		lyst.append(random.randint(1,11))
	print(lyst)
	mergesort(lyst)
	print(lyst)

if __name__ =='__main__':
	main()
		
