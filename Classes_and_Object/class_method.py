class Student:
    div="TE5"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def print(self):
        print(self.name)
        print(self.roll)

    @classmethod
    def set_div(cls,div):
        cls.div=div

    @classmethod
    def from_string(cls,std_string):
        name,roll=std_string.split('-')
        return cls(name,roll)
s1=Student('saurabh',69)
Student.set_div("TE6")
print(s1.__dict__)
print(s1.div)
print(Student.div)

student_data="Saurabh-69"
s2=Student.from_string(student_data)
print(s2.__dict__)

