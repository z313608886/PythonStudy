def fib1(n):
	if n > 2:
		return fib1(n-1) + fib1(n-2)
	else:
		return 1


def fib2(n):
	first = 1
	second = 1
	sum1 = 1
	count = 3
	while n >= count:
		sum1 = first + second
		first = second
		second = sum1
		count += 1
	return sum1
	
def main():
	n = input()
	n = int(n)
	print(fib1(n))
	print(fib2(n))

if __name__ == '__main__':
	main()
