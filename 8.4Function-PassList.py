#Print number of even and odd numbers from string
def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            print(i, end=" ")
            even+=1
        else:
            odd+=1
    print()
    return even,odd

print()
lst1=[1,2,3,4,5,6,7,8,9]
even,odd = count(lst1)
print("even = {} and odd = {}".format(even,odd))





