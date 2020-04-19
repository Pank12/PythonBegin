
pos = 1

def search(list, n):
    for i in range(len(list)):
        if i == n:
            globals()['pos']=i
            return True
    return False

list=[2,4,6,8,5,9,5]
n=5
if search(list, n):
    print("Match Found at", pos)
else:
    print("Match not found")
