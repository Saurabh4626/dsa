from abc import  ABC,abstractmethod
class Automob(ABC):
    def __init__(self,no_of_wheels):
        print("automob created")
        self.no_of_wheels=no_of_wheels

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def no_of_wheels(self):
        return self.no_of_wheels

class Car(Automob):
    def start(self):
        pass

    def stop(self):
        pass

    def drive(self):
        pass
    def no_of_wheels(self):
        return super().no_of_wheels()
# a=Automob()
c=Car(4)
print(c.no_of_wheels)
