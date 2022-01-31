list1 = ["Ram","Sai","Karthik","Unnam"]
list2 = ["Daddy","Mom","Chitti"]
print(list1)
tuple1 = ("Ram","Sai","Karthik","Unnam")
print(tuple1)
print(list1[2])
print(tuple1[2])
print(list1.insert(4,"NewElement"))
print(list1)
print("Ram is located at index: ",tuple1.index("Ram"))
list1.append("Ram")
print(list1)

print("--------------------------------------------------------")
print("Items in the list are: ")
for item in list1:
    print(item)
print("--------------------------------------------------------")

list1.sort()
print(list1)
list1.append(list2)
print("Each and every element in the list is: ")
for i in range(len(list1)):
    print(list1[i])

print(list1[len(list1)-1][1])