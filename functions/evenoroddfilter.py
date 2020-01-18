lst = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda n: n % 2 == 0, lst))
print(result)
for i in result: print(i)