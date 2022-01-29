a,b = input("Enter 2 numbers separated by a space: ").split()
a,b =int(a), int(b)
try:
    print("a/b is: ",a/b)
except:
    print("Number cannot be divided by zero...")
