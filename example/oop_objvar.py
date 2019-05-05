class Robot:
    population = 0
    def __init__(self,name):
        self.name = name
        print('(initializing {})'.format(self.name))
        Robot.population += 1

    def die(self):
        print('{} is being destroyed'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{} was the last one.'.format(self.name))
        else:
            print('there are still {} robots working'.format(Robot.population))

    def say_hi(self):
        print('hello my name is {}'.format(self.name))

    @classmethod  #不能缺少！！！
    def how_many(cls):
        print('we have {} robots.'.format(cls.population))

droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('R3-D2')
droid2.say_hi()
Robot.how_many()

droid1.die()
droid2.die()

Robot.how_many()
