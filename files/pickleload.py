import pickle, student

f = open("student.dat", "rb")
obj = pickle.load(f)
obj.display()