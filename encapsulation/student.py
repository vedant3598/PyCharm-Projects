class Student:

    """def __init__(self):
        self.__id = 123
        self.__name = "John"

    def display(self):
        print(self.__id)
        print(self.__name)"""

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


s = Student()
s.setName("Vedant")
s.setId(123)
print(s.getName())
print(s.getId())

"""s.display()
print(s._Student__id)"""
