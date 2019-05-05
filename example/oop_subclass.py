class SchoolMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(initialized schoolmember:{})'.format(self.name))

    def tell(self):
        print('name:"{}" age:"{}"'.format(self.name,self.age),end="")

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('(initialized teacher:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary:"{}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print('(initialized student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('marks:"{}"'.format(self.marks))
t = Teacher('mrs.zzz',40,30000)
s = Student('mark',25,75)

print()

members = [t,s]
for member in members:
    member.tell()


