
def sort(num):
    for i in range(len(num)-1):
        min=i
        for j in range(i,len(num)):
            if num[j]<num[min]:
                min=j

        temp = num[i]
        num[i] = num[min]
        num[min] = temp

        print(num)

num = [5,3,8,6,7,2]
sort(num)
print(num)
