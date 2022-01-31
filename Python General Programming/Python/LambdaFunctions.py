from ast import Lambda


def myFunc(n):
    return n*2
print(myFunc(4))


#Using Lambda functions

x = lambda a : a*2
print(x(5))

#Using lamnbda function within other functions

def function(n):
    return lambda a:a*n

myDoubler = function(2)
print(myDoubler(5))

myTripler = function(3)
print(myTripler(5))