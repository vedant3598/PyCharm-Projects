def fact(n):
    if n == 0:
        return 1
    else:
        result = n * fact(n - 1)
    return result


print(fact(3))
