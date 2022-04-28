
def steps(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n ==2:
        return 2
    return steps(n-1)+steps(n-2)

def optimisedSteps(n):
    arr = [0]*n
    arr[0]=1
    arr[1]=2
    for i in range(2,n):
        arr[i]=arr[i-1]+arr[i-2]
    return(arr[n-1])

print(optimisedSteps(5))
print(steps(5))