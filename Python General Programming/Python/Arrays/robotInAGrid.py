
def robotInAGrid(m,n):
    if m==1 and n==1:
        return 1
    if (m>1 and n==1) or (m==1 and n>1) :
        return 1
    return robotInAGrid(m-1,n) + robotInAGrid(m,n-1)

print(robotInAGrid(3,7))


def optimised(m,n):

    arr = [[0]*n]*m
    if m==1 and n==1:
        return 1
    for i in range(0,m):
            arr[i][0] = 1
    for j in range(0,n):
            arr[0][j] = 1   
    for i in range(1,m):
            for j in range(1,n):
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
    return arr[m-1][n-1]
    #print(arr)

print(optimised(3,7))
