#Add 2 array using for loop:
from numpy import *

arr1 = array([1,2,3,4])
arr2 = array([5,6,7,8])
arr = empty(5)
for i in range(len(arr1)):
    arr[i]=arr1[i]+arr2[i]
print(arr)

#Max number of an array

arrm = array([4,2,7,1])

maxnum=arrm[0]
for e in range(len(arrm)):
    if arrm[e]>maxnum:
        maxnum=arrm[e]
print(maxnum)
