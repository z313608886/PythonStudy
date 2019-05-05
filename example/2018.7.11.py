import math
print('a', '   ', 'mysqrt(a)', '   ', 'math.sqrt(a)', '   ' 'diff')
for a in range(1,10):
    x=3
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < 0.00001:
            break
        x = y
    b = math.sqrt(a)
    diff = abs(b-x)
    print(a, '   ', x, '   ', b, '   ', diff)
