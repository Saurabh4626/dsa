class Vehicle:
    def __init__(self,color,speed):
        self.color=color
        self.__speed=speed
    def set(self,speed):
        self.__speed=speed
    def get(self):
        return self.__speed
    def print(self):
        print("Vehicle's print statement")
class Car(Vehicle):

    def __init__(self,color,speed,numGears,isConvertable):
        super().__init__(color,speed)
        self.numGears = numGears
        self.isConvertable = isConvertable
    def print(self):
        super().print()
        print("car's print statement")
c=Car("red",15,2,False)
c.print()
c.get()
