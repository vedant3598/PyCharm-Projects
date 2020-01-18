class Student:
    major = "CS"

    def __init__(self, rollNum, name):
        self.rollNum = rollNum
        self.name = name


s1 = Student(1, "Vedant")
s2 = Student(2, "Bill")
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Student.major)
