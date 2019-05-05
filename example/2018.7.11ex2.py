import math
def eval_loop():
    while True:
        a = input('please input something:')
        print(a)
        if a == 'done':
            break
        b = eval(a)
        print(b)

eval_loop()

