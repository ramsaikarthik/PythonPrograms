#Fibonacci Series

def fib(n):
    if n<=1:
        return 1
    return fib(n-1) + fib(n-2)


n=20
print(fib(n))