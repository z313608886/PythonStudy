def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(3, 0)

def daxiao(a,b):
    if a>b: #a>b 不正确 必须要在操作符左右两边加空格
        return 1
    if a == b:
        return 0
    else:
        return -1
a=input('input a:\n')
b=input('input b:\n')
c=daxiao(a,b)
print(c)
