from functools import reduce
#Normal function
def add_all(a,b):
    return a+b
alst = {1,4,6,3,7}
sum = reduce(add_all,alst)
print(sum)

#With the help of lambda
nums = {3,2,4,3,5,6,9,7,8}

evens = list(filter(lambda n:n%2 == 0, nums))
print(evens)
doubles = list(map(lambda n : n*2,evens))
print(doubles)
sum = reduce(lambda a,b : a+b, doubles)
print(sum)