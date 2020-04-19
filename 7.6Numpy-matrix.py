#Arrey-2D, 3D, Matrix

from numpy import *
arr1 = array([
            [1,2,3,6,2,9],
            [4,5,6,7,5,3]

        ])
arr2=arr1.flatten()         #This will make 2D/3D array to 1D
arr3 = arr2.reshape(2,2,3)  #To create 3D array

print("1D array: \n", arr2)
print("3D array: \n", arr3)

#Matrix:

arrm = array([
            [1,2,3,6],
            [4,5,6,7]

        ])
#m=matrix(arrm)
#m = matrix('1 2 3 6 ; 4 5 6 7')
#m = matrix('1 2 ; 3 6 ; 4 5 ; 6 7')

m = matrix('1 2 3 ; 6 4 5 ; 1 6 7')
print(m.min())
print(m.max())
print("Diagonal :\n", diagonal(m))
print("Matrix: \n", m)

#Multiply matrixes

m1 = matrix('1 2 3 ; 6 4 5 ; 1 6 7')
m2 = matrix('1 2 3 ; 6 4 5 ; 2 6 7')

m3 = m1 * m2;
print(m3)

# without python inbuilt function:
#Multiplication of 2 matrices by taking inputs from user:
#_____________________________________________________ 


from numpy import *

# taking inputs from user


a = int(input("enter number of rows for array A:"))
b = int(input("enter the number of columns for array a:"))

a1 = int(input("enter the number of rows for array B:"))
b1 = int(input("enter the number of columns for array B :"))

n1 = a*b
n2 = a1*b1
n3 = a*b1
A = zeros(n1, int).reshape(a, b)
B = zeros(n2, int).reshape(a1, b1)

print("enter values for Array A:")
for i in range(a):
    for j in range(b):
        val = int(input())
        A[i][j] = val


# printing Array A

print("Array A:")
for i in range(a):
    for j in range(b):
        print(A[i][j], end=" ")
    print()


print("enter the values for Array B:")
for i in range(a1):
    for j in range(b1):
        val = int(input())
        B[i][j] = val

# printing array B


print("Array B:")
for i in range(a1):
    for j in range(b1):
        print(B[i][j], end=" ")
    print()

arr = zeros(n3, int).reshape(a, b1)

# performing multiplication of 2 matrices


if b != a1:
    print("multiplication not possible")

else:

    add = 0
    for i in range(a):
        for j in range(b1):
            for k in range(b):
                add += A[i][k] * B[k][j]
            arr[i][j] = add
            add = 0


# printing final array


    print("final matrix is")
    for i in range(a):
        for j in range(b1):
            print(arr[i][j], end=" ")
        print()

