#1
from array import *
arr = array('i', [])
n = int(input("Enter the length of array elements: "))
for e in range(n):
    x=int(input("Enter the array elements: "))
    arr.append(x)
print(arr)
arr.remove(2)
print(arr)
#2 Reverse the array
newarr = array('i', [])
c=len(arr)
for j in range(c):
    y=arr[c-j-1]
    newarr.append(y)
print(newarr)

