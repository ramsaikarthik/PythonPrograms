def repeat(a):
    if a > 0:
        print(a)
        repeat(a - 5)
    else:
        print("0")

if __name__ == "__main__":
    a = int(input("Enter a number: "))
    repeat(a)