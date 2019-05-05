class Counter(object):
    #class variable
    instances = 0

    #Constructer
    def __init__(self):
        Counter.instances += 1
        self.reset()

    #Mutator methods
    def reset(self):
        self._value=0

    def increment(self,amount=1):
        self._value += amount

    def decrement(self,amount=1):
        self._value -= amount

    #Accessor methods
    def getvalue(self):
        return self._value

    def __str__(self):
        return str(self._value)

    def __eq__(self, other):
        if self is other:return True
        if type(self)!=type(other):return False
        return self._value == other._value

c1=Counter()
print(c1)
c1.getvalue()
str(c1)
c1.increment()
c1.increment(5)
c1.reset()
print(c1)
c2=Counter()
print(Counter.instances)
print(c1==c1)
print(c1==0)
print(c1==c2)
c2.increment(1)
print(c1==c2)
