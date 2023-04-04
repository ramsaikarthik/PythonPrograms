from operator import index


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
    print("{0}:{1}".format(list1.index(item)+1, item))
print("--------------------------------------------------------")

#The above code for calculating index becomes time consuming and costly when the list keeps growing.
#Hence in order to calculate the index, we can make use of enumerate in-build function in python

for number, item in enumerate(list1):
    print("{0}: {1}".format(number+1, item))


list1.sort()
print(list1)
list1.append(list2)
print("Each and every element in the list is: ")
for i in range(len(list1)):
    print(list1[i])

print(list1[len(list1)-1][1])


elements = [list1[i] for i in range(0, len(list1))]
print(elements)