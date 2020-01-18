class Car:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    class Engine:
        def __init__(self, number):
            self.number = number

        def start(self):
            print("Engine Started!")


c = Car("Honda", 2019)
e = c.Engine(123)
e.start()
