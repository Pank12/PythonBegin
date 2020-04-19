from array import *

vals = array('i', [3,2,5,3,8])
print(sorted(vals))
newArr = array(vals.typecode, (a*a for a in vals))
#vals.reverse()
#print(vals)
#print(vals.buffer_info())   #-- it give the address of array
#print(vals.typecode)

for i in range(len(vals)):
    print(vals[i])

for i in vals:
    print(i)

for i in newArr:
    print(i)

# With the help of while
i=0
while i<len(newArr):
    print(newArr[i])
    i+=1

n = 27
if n in range(6, 21) or n % 2 != 0:
    print("Weird")
else:
    print("Not Weird")
