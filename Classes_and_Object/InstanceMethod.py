class Student:
    def __init__(self,name,roll): ##here self is object that is being paased
        self.name=name  ##default attributes for every objects
        self.roll=roll
    def print(self):  ##instance method
        print(self.name)
        print(self.roll)
s1=Student('saurabh',69)
s1.print()
Student.print(s1)  ##gives same output as s1.print