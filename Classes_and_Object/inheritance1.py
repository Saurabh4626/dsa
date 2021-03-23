class Vehicle:
    def __init__(self,color,speed):
        self.color=color
        self.speed=speed
class Car(Vehicle):

    def __init__(self,color,speed,numGears,isConvertable):
        super().__init__(color,speed)
        self.numGears = numGears
        self.isConvertable = isConvertable
    def printCar(self):
        print("color",self.color)
        print("speed", self.speed)
        print("numGears", self.numGears)
        print("isConvertable", self.isConvertable)
c=Car("red",15,2,False)
c.printCar()
