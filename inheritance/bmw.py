from abc import abstractmethod, ABC
class BMW(ABC):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Below is an interface example
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year)
        # BMW.__init__(self, make, model, year) <- Another way to get access to parent class
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    # Overriding
    def start(self):
        super().start() # <- Getting access to parent function method using super()
        print("Button Start")

    def stop(self):
        super.stop()
        print("Button Stop")

    # Abstraction
    def drive(self):
        print("Three series is being driven.")

class FiveSeries(BMW):

    def __init__(self, parkingAssistantEnabled, make, model, year):
        super().__init__(make, model, year)
        self.parkingAssistantEnabled = parkingAssistantEnabled

    def start(self):
        super().start() # <- Getting access to parent function method using super()
        print("Remote Start")

    def stop(self):
        super.stop()
        print("Remote Stop")

    # Abstraction
    def drive(self):
        print("Five series is being driven.")

threeSeries1 = ThreeSeries(True, "BMW", "328i", "2019")
print(threeSeries1.cruiseControlEnabled)
print(threeSeries1.make)
print(threeSeries1.model)
print(threeSeries1.year)
threeSeries1.start()
threeSeries1.stop()
threeSeries1.display()
