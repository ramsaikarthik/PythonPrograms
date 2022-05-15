def repeat(a):
    if a > 0:
        print(a)
        repeat(a - 5)
    else:
        print("0")


value = int(input("Enter a number: "))
repeat(value)