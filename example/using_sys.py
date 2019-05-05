import sys
print('the command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nthe PYTHONPATH IS',sys.path,'\n')

#import function1

#function1.say_hello()
#print(function1.__version__)

dir(sys)
