
a,b = input("Enter the required number of rows and columns with space separated: ").split()
a = int(a)
b = int(b)
print(a,b)
arr = [[0 for i in range(a)] for j in range(b)]
arr2 = [[0]*a]*b
print(arr)
print(arr2)