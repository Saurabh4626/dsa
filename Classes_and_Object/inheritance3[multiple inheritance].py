# class1       class2  ......  classn
#     !           !              !
#     !           !              !
#     !___________!______________!
#                 !
#                 !
#              child class


class class1:
    def print(self):
        print("class 1")
class class2:
    def print(self):
        print("class 2")
class class3:
    def print(self):
        print("class 3")
class child(class1,class2,class3):
    pass
c=child()
c.print()

##to get order of methods
print(child.mro())
## [<class '__main__.child'>, <class '__main__.class1'>, <class '__main__.class2'>, <class '__main__.class3'>, <class 'object'>]
