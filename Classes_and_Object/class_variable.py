class Student:
    div="TE5"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def print(self):
        print(self.name)
        print(self.roll)
s1=Student('saurabh',69)


print(s1.__dict__)
print(Student.div)


print(s1.div)
# {'name': 'saurabh', 'roll': 69}
# dict wont show div as it's not instance method

print(len(s1.__dict__))
#gives len of instance variable