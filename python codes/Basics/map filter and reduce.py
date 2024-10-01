
# Map
def cube(x):
    return x*x*x

l = [1,2,3,5,8,9]

newl = list(map(cube,l))
print(newl)


# filter
def filter_fun(a):
    return a> 3
newnewl = list(filter(filter_fun,l))
print(newnewl)

#reduce
from functools import reduce
num =[15,55,66,32,87,96,14]
def mysum(x,y):
    return x+y

sum= reduce(mysum ,num)
print(sum)