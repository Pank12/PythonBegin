from numpy import *

arr = array([1,2,3,4,5])
arr = arr + 5       #It will add 5 in every array element
print(arr)

arr1 = array([1,2,3,4,5])
arr2 = array([1,2,3,4,5])
arr=arr1+arr2               #o/p: [2,4,6,8,10]

print(sum(arr))
print(max(arr))
print(sort(arr))

#Concatenate
print(concatenate([arr1,arr2]))

arr3 = arr1             #
arr3 = arr1.view()      #Swallow copy
arr3 = arr1.copy()      #Deep Copy
