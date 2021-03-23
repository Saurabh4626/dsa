from abc import  ABC,abstractmethod
class Automob(ABC):
    def __init__(self):
        print("automob created")

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class Car(Automob):
    def __init__(self,name):
        super().__init__()
        print("Car created")
        self.name=name
    def start(self):
        pass

    def stop(self):
        pass

    def drive(self):
        pass
# a=Automob()  ##gives error
c=Car("BMW")
