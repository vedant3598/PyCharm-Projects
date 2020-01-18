x = int(input("Enter a min number: "))
y = int(input("Enter a max number: "))

while (x <= y):
    if x % 2 == 0:
        x += 1
    else:
        print(x)
        x += 1
