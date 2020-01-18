import pickle, student

f = open("student.dat", "wb")
s = student.Student(123, "Vedant", 90)
pickle.dump(s, f)
f.close()