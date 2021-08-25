#Given an array of n integers in which each number is between 1 to n-1. Find efficient algo that returns duplicate of a number
lst = [1,3,2,2]
mySet = set(lst)

print(lst)
for i in lst:
    a = lst[i]
    lst[a] = -lst[abs(a)]
    print(lst[a])
print(lst)