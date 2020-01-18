try:
    num = int(input("Enter an even number: "))
    assert num % 2 == 0, "You have entered an invalid number."

except AssertionError as obj:
    print(obj)

print("After Assertion")

