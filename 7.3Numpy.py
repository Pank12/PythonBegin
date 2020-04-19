from numpy import *

arr = array([1, 2, 3, 4, 5.0])
print(arr.dtype)

arr = linspace(0,16,10) # here 0-16 will be devided in 10 part
print(arr)

arr = arange(1,11,2)    # here 2 is step eg [1,3,5,7...]
print(arr)

arr = logspace(1,40,5)  # it prints in log form
print(arr)

arr = zeros(5)
print(arr)

arr = ones(5, int)  #mention int otherwise by default you will get flot array
print(arr)
