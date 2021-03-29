class Student:
    div="TE5"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def print(self):
        print(self.name)
        print(self.roll)
    @staticmethod
    def is_holiday(day):
        if day=="Sunday":
            return True
        return False

s1=Student('saurabh',69)
print(s1.__dict__)
print(S.is_holiday("Sunday"))
