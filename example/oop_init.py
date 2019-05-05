class person:
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print('hello,my name is', self.name)

p = person('swaroop')
p.say_hi()
print(p)
