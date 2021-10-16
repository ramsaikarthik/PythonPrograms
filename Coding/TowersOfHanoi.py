# Towers of Hanoi Problem

def TowersOfHanoi(n, start, end, middle):
    if n==1:
        print("Move disk 1 from ", start," to ", end)
        return
    TowersOfHanoi(n-1, start, middle, end)
    print("Move disk ",n, " from ", start, " to ", end)
    TowersOfHanoi(n-1, middle, end, start)


n = 4
TowersOfHanoi(n,'A','B','C')