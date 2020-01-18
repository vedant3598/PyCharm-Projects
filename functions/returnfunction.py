def display():
    def message(x):
        return 5 + x
    return message


f = display()
print(f(5))
