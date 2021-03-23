# class1       class2  ......  classn
#     !           !              !
#     !           !              !
#     !___________!______________!
#                 !
#                 !
#              child class


class class1:
    def __init__(self):
        self.name="class1"
        super().__init__()
    def print(self):
        print(self.name)
class class2:
    def __init__(self):
        self.name="class2"
        super().__init__()
    def print(self):
        print(self.name)

class class3:
    def __init__(self):
        self.name="class3"
        super().__init__()
    def print(self):
        print(self.name)
class child(class1,class2,class3):
    def __init__(self):
        super().__init__()
    def print(self):
        print(self.name)

c=child()
c.print()

##to get order of methods
print(child.mro())
## [<class '__main__.child'>, <class '__main__.class1'>, <class '__main__.class2'>, <class '__main__.class3'>, <class 'object'>]
