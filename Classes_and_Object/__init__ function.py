class Student:
    def __init__(self,name,roll): ##here self is object that is being paased
        self.name=name  ##default attributes for every objects
        self.roll=roll
s1=Student('saurabh',69)
print(s1.__dict__)  ##{'name': 'saurabh', 'roll': 69}