class Vehicle:
    def __init__(self,color,speed):
        self.color=color
        self.__speed=speed  ## we can't access this attribute as it is made private
        ## so we will use getter and setter method to access private members
    def set(self,speed):
        self.__speed=speed
    def get(self):
        return self.__speed
class Car(Vehicle):

    def __init__(self,color,speed,numGears,isConvertable):
        super().__init__(color,speed)
        self.numGears = numGears
        self.isConvertable = isConvertable
    def printCar(self):
        print("color",self.color)
        print("speed", super().get()) ## or self.get()
        print("numGears", self.numGears)
        print("isConvertable", self.isConvertable)
c=Car("red",15,2,False)
c.printCar()
