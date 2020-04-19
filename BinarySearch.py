pos=-1

def search(list, n):
    l=0             #Lower Bound
    u=len(list)     #Upper bound
    while l<=u:
       mid=(l+u) // 2

       if list[mid] == n:
           globals()['pos'] = mid
           return True
       else:
           if list[mid] < n:
               l=mid+1
           else:
               u=mid-1
    return False

list1=[5,35,86,43,8,9,45,12,6]
list=sorted(list1)
print(list)
n=43
if search(list, n):
    print ("Found at", pos)
else:
    print("not found")


